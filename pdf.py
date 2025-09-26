from flask import Blueprint, jsonify, request, send_file
from src.models.appointment import Appointment
from src.models.prescription import Prescription
from src.services.pdf_service import pdf_service
import os
from datetime import datetime

pdf_bp = Blueprint('pdf', __name__)

@pdf_bp.route('/prescription/<token>/pdf', methods=['GET'])
def generate_prescription_pdf(token):
    """Generate and download PDF prescription for a given token"""
    try:
        # Find the appointment
        appointment = Appointment.query.filter_by(token=token).first()
        if not appointment:
            return jsonify({'error': 'Appointment not found'}), 404
        
        # Get prescriptions for this appointment
        prescriptions = Prescription.query.filter_by(appointment_id=appointment.id).all()
        if not prescriptions:
            return jsonify({'error': 'No prescriptions found for this appointment'}), 404
        
        # Prepare appointment data
        appointment_data = {
            'name': appointment.name,
            'phone': appointment.phone,
            'issue': appointment.issue,
            'token': appointment.token,
            'timestamp': appointment.timestamp
        }
        
        # Prepare prescriptions data
        prescriptions_data = []
        for prescription in prescriptions:
            prescriptions_data.append({
                'medicine': prescription.medicine,
                'dosage': prescription.dosage,
                'duration': prescription.duration
            })
        
        # Generate PDF in memory
        pdf_buffer = pdf_service.generate_prescription_buffer(appointment_data, prescriptions_data)
        
        # Create filename
        filename = f"prescription_{token}_{datetime.now().strftime('%Y%m%d')}.pdf"
        
        return send_file(
            pdf_buffer,
            as_attachment=True,
            download_name=filename,
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@pdf_bp.route('/prescription/<token>/pdf/generate', methods=['POST'])
def create_prescription_pdf_file(token):
    """Generate PDF file and return file path for WhatsApp sending"""
    try:
        # Find the appointment
        appointment = Appointment.query.filter_by(token=token).first()
        if not appointment:
            return jsonify({'error': 'Appointment not found'}), 404
        
        # Get prescriptions for this appointment
        prescriptions = Prescription.query.filter_by(appointment_id=appointment.id).all()
        if not prescriptions:
            return jsonify({'error': 'No prescriptions found for this appointment'}), 404
        
        # Prepare appointment data
        appointment_data = {
            'name': appointment.name,
            'phone': appointment.phone,
            'issue': appointment.issue,
            'token': appointment.token,
            'timestamp': appointment.timestamp
        }
        
        # Prepare prescriptions data
        prescriptions_data = []
        for prescription in prescriptions:
            prescriptions_data.append({
                'medicine': prescription.medicine,
                'dosage': prescription.dosage,
                'duration': prescription.duration
            })
        
        # Create output directory if it doesn't exist
        output_dir = os.path.join(os.path.dirname(__file__), '..', 'static', 'prescriptions')
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate PDF file
        filename = f"prescription_{token}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        output_path = os.path.join(output_dir, filename)
        
        pdf_service.generate_prescription_pdf(appointment_data, prescriptions_data, output_path)
        
        return jsonify({
            'success': True,
            'filename': filename,
            'file_path': output_path,
            'download_url': f'/static/prescriptions/{filename}'
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
