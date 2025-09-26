from fpdf import FPDF
from datetime import datetime
import os
import io

class PDFPrescriptionService:
    """
    Service for generating PDF prescriptions with doctor information using FPDF.
    """
    
    def __init__(self):
        self.doctor_info = {
            'name': 'Dr. Sarah Johnson',
            'qualification': 'MBBS, MD (Internal Medicine)',
            'registration_number': 'MED-2019-45678',
            'clinic_name': 'MediCare Health Center',
            'address': '123 Healthcare Avenue, Medical District',
            'city': 'New York, NY 10001',
            'phone': '+1 (555) 123-4567',
            'email': 'dr.sarah@medicare-clinic.com'
        }
    
    def generate_prescription_pdf(self, appointment_data, prescriptions, output_path):
        """
        Generate a professional PDF prescription
        
        Args:
            appointment_data: Dictionary containing patient and appointment information
            prescriptions: List of prescription dictionaries
            output_path: Path where the PDF will be saved
            
        Returns:
            str: Path to the generated PDF file
        """
        try:
            # Create PDF instance
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            
            # Header with clinic information
            pdf.set_font('Arial', 'B', 20)
            pdf.set_text_color(44, 62, 80)  # Dark blue
            pdf.cell(0, 15, self.doctor_info['clinic_name'], 0, 1, 'C')
            
            pdf.set_font('Arial', '', 12)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 8, self.doctor_info['address'], 0, 1, 'C')
            pdf.cell(0, 8, self.doctor_info['city'], 0, 1, 'C')
            pdf.cell(0, 8, f"Phone: {self.doctor_info['phone']} | Email: {self.doctor_info['email']}", 0, 1, 'C')
            
            # Horizontal line
            pdf.ln(10)
            pdf.set_draw_color(52, 152, 219)  # Blue
            pdf.line(20, pdf.get_y(), 190, pdf.get_y())
            pdf.ln(10)
            
            # Doctor information
            pdf.set_font('Arial', 'B', 14)
            pdf.cell(0, 8, self.doctor_info['name'], 0, 1)
            pdf.set_font('Arial', '', 11)
            pdf.cell(0, 6, self.doctor_info['qualification'], 0, 1)
            pdf.cell(0, 6, f"Registration No: {self.doctor_info['registration_number']}", 0, 1)
            pdf.ln(10)
            
            # Prescription title
            pdf.set_font('Arial', 'B', 24)
            pdf.set_text_color(44, 62, 80)
            pdf.cell(0, 15, 'MEDICAL PRESCRIPTION', 0, 1, 'C')
            pdf.set_text_color(0, 0, 0)
            pdf.ln(10)
            
            # Patient information
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(50, 8, 'Patient Name:', 0, 0)
            pdf.set_font('Arial', '', 12)
            pdf.cell(70, 8, appointment_data['name'], 0, 0)
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(30, 8, 'Date:', 0, 0)
            pdf.set_font('Arial', '', 12)
            pdf.cell(0, 8, datetime.now().strftime('%B %d, %Y'), 0, 1)
            
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(50, 8, 'Phone:', 0, 0)
            pdf.set_font('Arial', '', 12)
            pdf.cell(70, 8, appointment_data['phone'], 0, 0)
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(30, 8, 'Token No:', 0, 0)
            pdf.set_font('Arial', '', 12)
            pdf.cell(0, 8, appointment_data['token'], 0, 1)
            
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(50, 8, 'Chief Complaint:', 0, 0)
            pdf.set_font('Arial', '', 12)
            pdf.multi_cell(0, 8, appointment_data['issue'])
            pdf.ln(5)
            
            # Prescription section
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 12, 'PRESCRIPTION', 0, 1)
            pdf.ln(5)
            
            # Table header
            pdf.set_font('Arial', 'B', 11)
            pdf.set_fill_color(52, 152, 219)  # Blue background
            pdf.set_text_color(255, 255, 255)  # White text
            pdf.cell(15, 10, 'S.No.', 1, 0, 'C', True)
            pdf.cell(60, 10, 'Medicine Name', 1, 0, 'C', True)
            pdf.cell(60, 10, 'Dosage Instructions', 1, 0, 'C', True)
            pdf.cell(35, 10, 'Duration', 1, 1, 'C', True)
            
            # Table content
            pdf.set_font('Arial', '', 10)
            pdf.set_text_color(0, 0, 0)
            pdf.set_fill_color(248, 249, 250)  # Light gray
            
            for i, prescription in enumerate(prescriptions, 1):
                fill = i % 2 == 0  # Alternate row colors
                pdf.cell(15, 10, str(i), 1, 0, 'C', fill)
                pdf.cell(60, 10, prescription['medicine'][:25], 1, 0, 'L', fill)
                pdf.cell(60, 10, prescription['dosage'][:25], 1, 0, 'L', fill)
                pdf.cell(35, 10, prescription['duration'][:15], 1, 1, 'L', fill)
            
            pdf.ln(15)
            
            # Instructions
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(0, 8, 'General Instructions:', 0, 1)
            pdf.set_font('Arial', '', 10)
            instructions = [
                '• Take medicines as prescribed by the doctor',
                '• Complete the full course of medication',
                '• Consult the doctor if any adverse reactions occur',
                '• Follow up as advised'
            ]
            for instruction in instructions:
                pdf.cell(0, 6, instruction, 0, 1)
            
            pdf.ln(20)
            
            # Doctor signature section
            pdf.set_font('Arial', 'B', 11)
            pdf.cell(100, 8, '', 0, 0)  # Empty space
            pdf.cell(70, 8, "Doctor's Signature", 0, 1, 'C')
            pdf.ln(15)
            pdf.cell(100, 8, '', 0, 0)  # Empty space
            pdf.line(120, pdf.get_y(), 180, pdf.get_y())  # Signature line
            pdf.ln(8)
            pdf.set_font('Arial', '', 10)
            pdf.cell(100, 6, '', 0, 0)  # Empty space
            pdf.cell(70, 6, f"Dr. {self.doctor_info['name']}", 0, 1, 'C')
            pdf.cell(100, 6, '', 0, 0)  # Empty space
            pdf.cell(70, 6, self.doctor_info['qualification'], 0, 1, 'C')
            
            pdf.ln(10)
            
            # Footer
            pdf.set_font('Arial', '', 8)
            pdf.set_text_color(128, 128, 128)
            pdf.cell(0, 6, 'This prescription is generated electronically and is valid for medical purposes.', 0, 1, 'C')
            pdf.cell(0, 6, f"For any queries, please contact {self.doctor_info['phone']} or {self.doctor_info['email']}", 0, 1, 'C')
            
            # Save PDF
            pdf.output(output_path)
            
            return output_path
            
        except Exception as e:
            raise Exception(f"Error generating PDF: {str(e)}")
    
    def generate_prescription_buffer(self, appointment_data, prescriptions):
        """
        Generate PDF prescription in memory buffer
        
        Args:
            appointment_data: Dictionary containing patient and appointment information
            prescriptions: List of prescription dictionaries
            
        Returns:
            io.BytesIO: PDF content as bytes buffer
        """
        buffer = io.BytesIO()
        
        # Create temporary file path
        temp_path = f"/tmp/prescription_{appointment_data['token']}.pdf"
        
        try:
            # Generate PDF to temporary file
            self.generate_prescription_pdf(appointment_data, prescriptions, temp_path)
            
            # Read file content into buffer
            with open(temp_path, 'rb') as f:
                buffer.write(f.read())
            
            # Clean up temporary file
            if os.path.exists(temp_path):
                os.remove(temp_path)
            
            buffer.seek(0)
            return buffer
            
        except Exception as e:
            # Clean up temporary file in case of error
            if os.path.exists(temp_path):
                os.remove(temp_path)
            raise e

# Global instance
pdf_service = PDFPrescriptionService()
