# Doctor Appointment and Prescription Application - Final Documentation

## Overview

This document outlines the features, architecture, and usage of the Doctor Appointment and Prescription application. The application facilitates patient appointment booking, doctor prescription management, and automated prescription delivery via WhatsApp, now with PDF support.

## Key Features

1.  **Patient Portal (Publicly Accessible)**:
    *   Patients can book appointments by providing their name, phone number, and health issue.
    *   Upon successful booking, a unique, incremental token number (date-based) is generated and displayed to the patient.
    *   Patients receive their prescription via WhatsApp once the doctor completes the consultation.

2.  **Doctor Dashboard (Authenticated Access)**:
    *   Doctors can log in using basic authentication (username/password).
    *   The dashboard displays a list of all booked appointments with their unique token numbers.
    *   Doctors can click on an appointment to view patient details and fill out prescription information.
    *   **Medicine Templates (Sidebar)**: A sidebar provides pre-defined medicine templates for common health issues, allowing doctors to quickly populate prescription fields with a single click.
    *   Doctors can add, modify, or remove medicines from the prescription.
    *   Upon submitting the prescription, an authentic PDF report is generated with doctor information.
    *   The generated PDF prescription is automatically sent to the patient's registered WhatsApp number.

3.  **Incremental Token Numbers**:
    *   Appointment tokens are now generated incrementally, prefixed with the current date (e.g., `YYYYMMDDNNN`).

4.  **PDF Prescription Generation**:
    *   Prescriptions are generated as professional PDF documents, including:
        *   Clinic and doctor information (name, qualification, registration, contact details).
        *   Patient details (name, phone, health issue, token).
        *   A structured table of prescribed medicines (name, dosage, duration).
        *   General instructions and doctor's signature section.

5.  **WhatsApp Integration**:
    *   Patients receive their appointment tokens and final PDF prescriptions directly on their WhatsApp number.

## Application Architecture

The application is built using a Flask backend for API services and a simple HTML/CSS/JavaScript frontend for the user interface.

*   **Backend**: Flask (Python)
    *   **Database**: SQLite (for simplicity, can be extended to PostgreSQL/MySQL)
    *   **Models**: `Appointment`, `Prescription`
    *   **Services**: `whatsapp_service.py`, `pdf_service.py`, `auth_service.py`, `medicine_templates.py`
    *   **Routes**: `appointment.py`, `prescription.py`, `auth.py`, `templates.py`, `pdf.py`
*   **Frontend**: HTML, CSS, JavaScript
    *   Separated Patient Portal (public) and Doctor Dashboard (authenticated).
    *   Responsive design for optimal viewing on various devices.

## Deployment

The application is deployed and accessible at: [https://19hninc09je8.manus.space](https://19hninc09je8.manus.space)

## Usage Instructions

### For Patients

1.  Navigate to the application URL: [https://19hninc09je8.manus.space](https://19hninc09je8.manus.space)
2.  Fill in your **Full Name**, **Phone Number**, and **Health Issue** in the "Book Your Appointment" section.
3.  Click the "Book Appointment" button.
4.  You will receive a unique token number. Please save this token.
5.  Once the doctor completes your consultation, you will receive a PDF prescription on your provided WhatsApp number.

### For Doctors

1.  Navigate to the application URL: [https://19hninc09je8.manus.space](https://19hninc09je8.manus.space)
2.  Click on the "Doctor Login" button.
3.  Enter your credentials:
    *   **Username**: `doctor`
    *   **Password**: `password123`
4.  Click the "Login" button.
5.  On the Doctor Dashboard, you will see a list of appointments.
6.  Click on an appointment card to view details and create a prescription.
7.  Use the "Medicine Templates" sidebar on the left to quickly apply pre-defined medicine lists for common issues.
8.  Adjust or add more medicines as needed using the input fields.
9.  Click "Send Prescription" to generate the PDF and send it to the patient via WhatsApp.

## Future Enhancements

*   **User Management**: Implement a more robust user management system for doctors (e.g., registration, password reset).
*   **Appointment Scheduling**: Allow patients to select preferred dates and times for appointments.
*   **Notification System**: Enhance WhatsApp integration with appointment reminders and status updates.
*   **Advanced PDF Customization**: Allow doctors to customize their clinic information and logo in the PDF.
*   **Database Integration**: Migrate from SQLite to a more robust database like PostgreSQL for production environments.
*   **Admin Panel**: Create an admin panel for managing doctors, patients, and templates.

## References

*   [Flask Documentation](https://flask.palletsprojects.com/)
*   [FPDF2 Documentation](https://pyfpdf.github.io/fpdf2/)
*   [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

---

**Author**: Manus AI
**Date**: September 25, 2025
