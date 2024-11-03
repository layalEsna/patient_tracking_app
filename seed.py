
from models.patient import Patient
from models.doctor import Doctor

def seed_database():
    """Seeds the database with initial data and creates necessary tables if they do not already exist."""
    
    # Create tables if they do not exist
    Patient.create_table()
    Doctor.create_table()

    # Check if there are already doctors in the database
    if not Doctor.get_all():  
        print("Seeding doctors...")
        doctor_1 = Doctor.create("Dr. Joe", "Walter", "Cardiology")
        doctor_2 = Doctor.create("Dr. Sam", "Smith", "Rheumatology")
        doctor_3 = Doctor.create("Dr. Bob", "Moore", "Oncology")

        print("Seeding patients...")
        Patient.create("John", "Doe", 45, disease="Hypertension", doctor_id=doctor_1.id)
        Patient.create("Jane", "Smith", 65, disease="Arthritis", doctor_id=doctor_2.id)
        Patient.create("Emily", "Johnson", 28, disease="Diabetes", doctor_id=doctor_3.id)
        
        print("Database seeded successfully.")
    else:
        print("Data already exists. Skipping seeding.")

if __name__ == "__main__":
    seed_database()

# PYTHONPATH=. python -m utils.cli