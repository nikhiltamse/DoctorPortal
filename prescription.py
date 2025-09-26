from src.models.user import db

class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'), nullable=False)
    medicine = db.Column(db.String(200), nullable=False)
    dosage = db.Column(db.String(200), nullable=False)  # When to take (e.g., "Morning and Evening")
    duration = db.Column(db.String(100), nullable=False)  # Duration of course (e.g., "7 days")

    def __repr__(self):
        return f'<Prescription {self.medicine}>'

    def to_dict(self):
        return {
            'id': self.id,
            'appointment_id': self.appointment_id,
            'medicine': self.medicine,
            'dosage': self.dosage,
            'duration': self.duration
        }
