from flask import Blueprint, jsonify, request
from src.models.appointment import Appointment, db

appointment_bp = Blueprint('appointment', __name__)

@appointment_bp.route('/appointments', methods=['POST'])
def create_appointment():
    """Create a new appointment and return the generated token"""
    try:
        data = request.json
        
        # Validate required fields
        if not data or not all(key in data for key in ['name', 'phone', 'issue']):
            return jsonify({'error': 'Missing required fields: name, phone, issue'}), 400
        
        # Create new appointment
        appointment = Appointment(
            name=data['name'].strip(),
            phone=data['phone'].strip(),
            issue=data['issue'].strip()
        )
        
        db.session.add(appointment)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'token': appointment.token,
            'message': 'Appointment booked successfully'
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@appointment_bp.route('/appointments', methods=['GET'])
def get_appointments():
    """Get all appointments for the doctor dashboard"""
    try:
        appointments = Appointment.query.order_by(Appointment.timestamp.desc()).all()
        return jsonify([appointment.to_dict() for appointment in appointments])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@appointment_bp.route('/appointments/<string:token>', methods=['GET'])
def get_appointment_by_token(token):
    """Get a specific appointment by token"""
    try:
        appointment = Appointment.query.filter_by(token=token).first_or_404()
        return jsonify(appointment.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
