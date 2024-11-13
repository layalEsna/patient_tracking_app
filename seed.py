# seed.py


from models.patient import Patient
from models.doctor import Doctor



def seed_database(reset=False):
    if reset:
        Patient.drop_table()
        Doctor.drop_table()
        Patient.create_table()
        Doctor.create_table()
    if not Doctor.get_all():
        print("Seeding doctors...")
        doctor_1 = Doctor.create("Dr. Joe", "Walter", "Cardiology")
        doctor_2 = Doctor.create("Dr. Sam", "Smith", "Rheumatology")
        doctor_3 = Doctor.create("Dr. Bob", "Moore", "Oncology")
        doctor_3 = Doctor.create("Dr. hhhhh", "fffff", "fffff")
    if not Patient.get_all():
        print("Seeding patients...")
        Patient.create("Elon", "shi", 45, disease="Hypertension", doctor_id=doctor_1.id)
        Patient.create("Jane", "Smith", 65, disease="Arthritis", doctor_id=doctor_2.id)
        Patient.create("Emily", "Johnson", 28, disease="Diabetes", doctor_id=doctor_3.id)
        Patient.create("ddddd", "Jddddd", 28, disease="Diabetes", doctor_id=doctor_3.id)
    else:

        print("Database seeded successfully.")

if __name__ == "__main__":
    seed_database(reset=True)

