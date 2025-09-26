# Doctor Appointment and Prescription App: System Design

## 1. Introduction

This document outlines the system design for a web-based doctor appointment and prescription management application. The application will facilitate a seamless workflow for patients to book appointments and for doctors to manage prescriptions, with a key feature being the delivery of prescriptions via WhatsApp.

## 2. Functional Requirements

The application will have two main interfaces: a patient-facing page for booking appointments and a doctor-facing dashboard for managing appointments and prescriptions.

### 2.1. Patient Interface

*   **Appointment Booking:** Patients can book an appointment by providing their name, phone number, and a brief description of their health issue.
*   **Token Generation:** Upon successful submission of the appointment form, a unique token will be generated and displayed to the patient.
*   **Prescription Notification:** Patients will receive their prescription details via WhatsApp, linked to their registered phone number and appointment token.

### 2.2. Doctor Interface

*   **Appointment Dashboard:** Doctors will have access to a dashboard that displays a list of all appointments, identified by their unique tokens.
*   **Prescription Management:** Doctors can select an appointment token to view the patient's details and fill out a prescription form.
*   **Prescription Form:** The prescription form will include fields for the medicine name, dosage instructions (e.g., when to take the medicine), and the duration of the course.
*   **Record Creation:** Upon submitting the prescription, the information will be saved to the database, and the prescription will be sent to the patient's WhatsApp number.

## 3. Non-Functional Requirements

*   **Security:** All patient data must be handled securely, and the application should be protected against common web vulnerabilities.
*   **Usability:** The user interfaces for both patients and doctors should be intuitive and easy to use.
*   **Scalability:** The application should be designed to handle a growing number of users and appointments.
*   **Reliability:** The system should be reliable, ensuring that appointments are not lost and prescriptions are delivered promptly.

## 4. System Architecture

The application will be built using a client-server architecture.

*   **Frontend:** The frontend will be built using HTML, CSS, and JavaScript. It will consist of two pages: the patient booking page and the doctor's dashboard.
*   **Backend:** The backend will be a Flask-based web server that will handle the business logic, interact with the database, and integrate with the WhatsApp messaging API.
*   **Database:** A SQLite database will be used to store appointment and prescription data. This is a lightweight and easy-to-use database that is suitable for this application.
*   **WhatsApp Integration:** A third-party service like Twilio will be used to send WhatsApp messages.

## 5. Data Model

The database will consist of two main tables: `Appointments` and `Prescriptions`.

### 5.1. Appointments Table

| Column        | Data Type | Description                                   |
|---------------|-----------|-----------------------------------------------|
| `id`          | Integer   | Primary Key                                   |
| `token`       | String    | Unique token for the appointment              |
| `name`        | String    | Patient's name                                |
| `phone`       | String    | Patient's phone number                        |
| `issue`       | String    | Patient's health issue                        |
| `timestamp`   | DateTime  | Time of appointment creation                  |

### 5.2. Prescriptions Table

| Column        | Data Type | Description                                   |
|---------------|-----------|-----------------------------------------------|
| `id`          | Integer   | Primary Key                                   |
| `appointment_id` | Integer   | Foreign Key to the Appointments table         |
| `medicine`    | String    | Name of the prescribed medicine               |
| `dosage`      | String    | When to take the medicine (e.g., morning, evening) |
| `duration`    | String    | Duration of the course (e.g., 7 days)         |

## 6. API Endpoints

The Flask backend will expose the following RESTful API endpoints:

*   `POST /api/appointments`: Creates a new appointment.
*   `GET /api/appointments`: Retrieves a list of all appointments for the doctor's dashboard.
*   `POST /api/prescriptions`: Creates a new prescription for an appointment.

## 7. Technology Stack

*   **Frontend:** HTML, CSS, JavaScript
*   **Backend:** Flask (Python)
*   **Database:** SQLite
*   **WhatsApp Integration:** Twilio API (or a similar service)

