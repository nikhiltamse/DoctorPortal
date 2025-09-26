import os
from typing import List, Dict
from datetime import datetime

class WhatsAppService:
    """
    WhatsApp messaging service for sending prescription details and PDF files.
    This is a mock implementation that simulates WhatsApp message sending.
    In production, you would integrate with Twilio WhatsApp API or WhatsApp Business API.
    """
    
    def __init__(self):
        # In production, these would be environment variables
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID', 'mock_account_sid')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN', 'mock_auth_token')
        self.whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER', 'whatsapp:+14155238886')
        self.mock_mode = True  # Set to False when using real Twilio credentials
        self.log_file = '/home/ubuntu/doctor_appointment_app/whatsapp_messages.log'
    
    def send_prescription(self, patient_name: str, phone_number: str, token: str, prescriptions: List[Dict]) -> bool:
        """
        Send prescription details to patient via WhatsApp
        
        Args:
            patient_name: Name of the patient
            phone_number: Patient's phone number
            token: Appointment token
            prescriptions: List of prescription dictionaries
            
        Returns:
            bool: True if message sent successfully, False otherwise
        """
        try:
            message = self._format_prescription_message(patient_name, token, prescriptions)
            
            if self.mock_mode:
                return self._send_mock_message(phone_number, message)
            else:
                return self._send_twilio_message(phone_number, message)
                
        except Exception as e:
            print(f"Error sending WhatsApp message: {str(e)}")
            return False
    
    def send_prescription_pdf(self, patient_name: str, phone_number: str, token: str, pdf_file_path: str) -> Dict:
        """
        Send prescription PDF to patient via WhatsApp
        
        Args:
            patient_name: Name of the patient
            phone_number: Patient's phone number
            token: Appointment token
            pdf_file_path: Path to the PDF file
            
        Returns:
            dict: Result of the PDF sending operation
        """
        try:
            # Check if PDF file exists
            if not os.path.exists(pdf_file_path):
                return {
                    'success': False,
                    'error': 'PDF file not found'
                }
            
            # Get file size for logging
            file_size = os.path.getsize(pdf_file_path)
            file_size_mb = file_size / (1024 * 1024)
            
            message = self._format_pdf_message(patient_name, token)
            
            if self.mock_mode:
                return self._send_mock_pdf(phone_number, message, pdf_file_path, file_size_mb)
            else:
                return self._send_twilio_pdf(phone_number, message, pdf_file_path)
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _format_prescription_message(self, patient_name: str, token: str, prescriptions: List[Dict]) -> str:
        """Format the prescription message for WhatsApp"""
        message = f"🏥 *MediCare Prescription*\n\n"
        message += f"Dear {patient_name},\n\n"
        message += f"Your prescription for appointment token *{token}* is ready:\n\n"
        
        for i, prescription in enumerate(prescriptions, 1):
            message += f"*{i}. {prescription['medicine']}*\n"
            message += f"   📋 Dosage: {prescription['dosage']}\n"
            message += f"   ⏰ Duration: {prescription['duration']}\n\n"
        
        message += "Please follow the prescribed dosage and duration.\n"
        message += "If you have any questions, please contact your doctor.\n\n"
        message += "Thank you for choosing MediCare! 🩺"
        
        return message
    
    def _format_pdf_message(self, patient_name: str, token: str) -> str:
        """Format the PDF message for WhatsApp"""
        message = f"🏥 *MediCare Health Center*\n"
        message += f"📋 *Prescription PDF for {patient_name}*\n\n"
        message += f"Token: {token}\n"
        message += f"Date: {datetime.now().strftime('%B %d, %Y')}\n\n"
        message += f"📄 Please find your prescription PDF attached.\n\n"
        message += f"📝 *Important Notes:*\n"
        message += f"• Keep this prescription for your records\n"
        message += f"• Show this to the pharmacist when purchasing medicines\n"
        message += f"• Follow the dosage instructions carefully\n"
        message += f"• Contact us for any clarifications\n\n"
        message += f"For queries, contact: +1 (555) 123-4567\n\n"
        message += f"*Dr. Sarah Johnson*\n"
        message += f"MBBS, MD (Internal Medicine)\n"
        message += f"MediCare Health Center"
        
        return message
    
    def _send_mock_message(self, phone_number: str, message: str) -> bool:
        """
        Mock WhatsApp message sending for development/demo purposes
        """
        print("=" * 50)
        print("📱 MOCK WHATSAPP MESSAGE SENT")
        print("=" * 50)
        print(f"To: {phone_number}")
        print(f"Message:\n{message}")
        print("=" * 50)
        
        # Log the message to a file for demo purposes
        try:
            with open(self.log_file, 'a') as f:
                f.write(f"\n{'='*50}\n")
                f.write(f"Timestamp: {datetime.now()}\n")
                f.write(f"To: {phone_number}\n")
                f.write(f"Message:\n{message}\n")
                f.write(f"{'='*50}\n")
        except Exception as e:
            print(f"Error logging message: {e}")
        
        return True
    
    def _send_mock_pdf(self, phone_number: str, message: str, pdf_file_path: str, file_size_mb: float) -> Dict:
        """
        Mock WhatsApp PDF sending for development/demo purposes
        """
        print("=" * 50)
        print("📱 MOCK WHATSAPP PDF SENT")
        print("=" * 50)
        print(f"To: {phone_number}")
        print(f"Message:\n{message}")
        print(f"📎 Attachment: {os.path.basename(pdf_file_path)} ({file_size_mb:.2f} MB)")
        print("=" * 50)
        
        # Log the PDF message
        try:
            with open(self.log_file, 'a') as f:
                f.write(f"\n{'='*50}\n")
                f.write(f"PDF MESSAGE - Timestamp: {datetime.now()}\n")
                f.write(f"To: {phone_number}\n")
                f.write(f"Message:\n{message}\n")
                f.write(f"PDF File: {pdf_file_path} ({file_size_mb:.2f} MB)\n")
                f.write(f"{'='*50}\n")
        except Exception as e:
            print(f"Error logging PDF message: {e}")
        
        return {
            'success': True,
            'message': 'Prescription PDF sent successfully via WhatsApp',
            'phone': phone_number,
            'file_size': f"{file_size_mb:.2f} MB"
        }
    
    def _send_twilio_message(self, phone_number: str, message: str) -> bool:
        """
        Send actual WhatsApp message using Twilio API
        Uncomment and configure when ready to use with real Twilio credentials
        """
        # from twilio.rest import Client
        
        # try:
        #     client = Client(self.account_sid, self.auth_token)
        #     
        #     # Format phone number for WhatsApp
        #     to_whatsapp = f"whatsapp:{phone_number}"
        #     
        #     message = client.messages.create(
        #         body=message,
        #         from_=self.whatsapp_number,
        #         to=to_whatsapp
        #     )
        #     
        #     print(f"WhatsApp message sent successfully. SID: {message.sid}")
        #     return True
        #     
        # except Exception as e:
        #     print(f"Error sending Twilio WhatsApp message: {str(e)}")
        #     return False
        
        # For now, fall back to mock
        return self._send_mock_message(phone_number, message)
    
    def _send_twilio_pdf(self, phone_number: str, message: str, pdf_file_path: str) -> Dict:
        """
        Send actual WhatsApp PDF using Twilio API
        Uncomment and configure when ready to use with real Twilio credentials
        """
        # from twilio.rest import Client
        
        # try:
        #     client = Client(self.account_sid, self.auth_token)
        #     
        #     # Format phone number for WhatsApp
        #     to_whatsapp = f"whatsapp:{phone_number}"
        #     
        #     # Upload media first
        #     with open(pdf_file_path, 'rb') as f:
        #         media = client.media.create(
        #             content_type='application/pdf',
        #             body=f.read()
        #         )
        #     
        #     # Send message with media
        #     message = client.messages.create(
        #         body=message,
        #         media_url=[media.uri],
        #         from_=self.whatsapp_number,
        #         to=to_whatsapp
        #     )
        #     
        #     print(f"WhatsApp PDF sent successfully. SID: {message.sid}")
        #     return {
        #         'success': True,
        #         'message': 'PDF sent successfully via WhatsApp',
        #         'phone': phone_number,
        #         'sid': message.sid
        #     }
        #     
        # except Exception as e:
        #     print(f"Error sending Twilio WhatsApp PDF: {str(e)}")
        #     return {
        #         'success': False,
        #         'error': str(e)
        #     }
        
        # For now, fall back to mock
        file_size = os.path.getsize(pdf_file_path)
        file_size_mb = file_size / (1024 * 1024)
        return self._send_mock_pdf(phone_number, message, pdf_file_path, file_size_mb)

# Global instance
whatsapp_service = WhatsAppService()
