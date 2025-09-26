class MedicineTemplatesService:
    """
    Service for managing medicine templates for common health issues.
    Doctors can quickly select templates and customize as needed.
    """
    
    def __init__(self):
        self.templates = {
            'fever_headache': {
                'name': 'Fever & Headache',
                'description': 'Common treatment for fever and headache symptoms',
                'medicines': [
                    {
                        'medicine': 'Paracetamol 500mg',
                        'dosage': 'Every 6 hours as needed',
                        'duration': '3-5 days'
                    },
                    {
                        'medicine': 'Ibuprofen 400mg',
                        'dosage': 'Every 8 hours with food',
                        'duration': '3 days'
                    }
                ]
            },
            'cough_cold': {
                'name': 'Cough & Cold',
                'description': 'Treatment for cough, cold, and respiratory symptoms',
                'medicines': [
                    {
                        'medicine': 'Dextromethorphan Syrup',
                        'dosage': '2 teaspoons every 6 hours',
                        'duration': '5-7 days'
                    },
                    {
                        'medicine': 'Cetirizine 10mg',
                        'dosage': 'Once daily at bedtime',
                        'duration': '5 days'
                    },
                    {
                        'medicine': 'Vitamin C 500mg',
                        'dosage': 'Once daily with breakfast',
                        'duration': '7 days'
                    }
                ]
            },
            'stomach_upset': {
                'name': 'Stomach Upset',
                'description': 'Treatment for stomach pain, acidity, and digestive issues',
                'medicines': [
                    {
                        'medicine': 'Omeprazole 20mg',
                        'dosage': 'Once daily before breakfast',
                        'duration': '5 days'
                    },
                    {
                        'medicine': 'Simethicone 40mg',
                        'dosage': 'After meals and at bedtime',
                        'duration': '3 days'
                    }
                ]
            },
            'allergic_reaction': {
                'name': 'Allergic Reaction',
                'description': 'Treatment for mild to moderate allergic reactions',
                'medicines': [
                    {
                        'medicine': 'Loratadine 10mg',
                        'dosage': 'Once daily',
                        'duration': '7 days'
                    },
                    {
                        'medicine': 'Hydrocortisone Cream 1%',
                        'dosage': 'Apply to affected area twice daily',
                        'duration': '5 days'
                    }
                ]
            },
            'back_pain': {
                'name': 'Back Pain',
                'description': 'Treatment for muscle pain and back ache',
                'medicines': [
                    {
                        'medicine': 'Diclofenac 50mg',
                        'dosage': 'Twice daily with food',
                        'duration': '5 days'
                    },
                    {
                        'medicine': 'Muscle Relaxant Gel',
                        'dosage': 'Apply to affected area 3 times daily',
                        'duration': '7 days'
                    }
                ]
            },
            'hypertension': {
                'name': 'High Blood Pressure',
                'description': 'Basic treatment for hypertension management',
                'medicines': [
                    {
                        'medicine': 'Amlodipine 5mg',
                        'dosage': 'Once daily in the morning',
                        'duration': '30 days (continue as prescribed)'
                    },
                    {
                        'medicine': 'Lifestyle modifications',
                        'dosage': 'Low salt diet, regular exercise',
                        'duration': 'Ongoing'
                    }
                ]
            },
            'diabetes_management': {
                'name': 'Diabetes Management',
                'description': 'Basic diabetes medication and monitoring',
                'medicines': [
                    {
                        'medicine': 'Metformin 500mg',
                        'dosage': 'Twice daily with meals',
                        'duration': '30 days (continue as prescribed)'
                    },
                    {
                        'medicine': 'Blood glucose monitoring',
                        'dosage': 'Check twice daily (fasting & post-meal)',
                        'duration': 'Daily'
                    }
                ]
            },
            'skin_infection': {
                'name': 'Skin Infection',
                'description': 'Treatment for minor skin infections and wounds',
                'medicines': [
                    {
                        'medicine': 'Antibiotic Ointment',
                        'dosage': 'Apply to affected area twice daily',
                        'duration': '7 days'
                    },
                    {
                        'medicine': 'Antiseptic Solution',
                        'dosage': 'Clean wound before applying ointment',
                        'duration': '7 days'
                    }
                ]
            }
        }
    
    def get_all_templates(self):
        """Get all available medicine templates"""
        return [
            {
                'id': template_id,
                'name': template['name'],
                'description': template['description'],
                'medicine_count': len(template['medicines'])
            }
            for template_id, template in self.templates.items()
        ]
    
    def get_template(self, template_id: str):
        """Get a specific template by ID"""
        if template_id not in self.templates:
            return None
        
        return {
            'id': template_id,
            **self.templates[template_id]
        }
    
    def search_templates(self, query: str):
        """Search templates by name or description"""
        query = query.lower()
        results = []
        
        for template_id, template in self.templates.items():
            if (query in template['name'].lower() or 
                query in template['description'].lower()):
                results.append({
                    'id': template_id,
                    'name': template['name'],
                    'description': template['description'],
                    'medicine_count': len(template['medicines'])
                })
        
        return results

# Global instance
medicine_templates_service = MedicineTemplatesService()
