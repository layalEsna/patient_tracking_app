from models.patient import Patient
from models.doctor import Doctor

def seed_data():
    Patient.drop_table()
    Doctor.drop_table()

    Patient.create_table()
    Doctor.create_table()

    doctor1 = Doctor.create(name='Dr. Joe', lastname='Walter', specialty='Cardiology')
    doctor2 = Doctor.create(name='Dr. Sam', lastname='Smith', specialty='Rheumatologist')
    doctor3 = Doctor.create(name='Dr. Bob', lastname='More', specialty='Oncologists')

    Patient.create(name='Samy', lastname='Von', age=34, disease='Hypertension', doctor_id=doctor1.id)
    Patient.create(name='Jane', lastname='Sue', age=65, disease='Arthritis', doctor_id=doctor3.id)
    Patient.create(name='Zane', lastname='Shane', age=47, disease='Diabetes', doctor_id=doctor2.id)


if __name__ == "__main__":
    seed_data()
    print("Seeded database")
