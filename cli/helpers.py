# helpers.py

from models.patient import Patient
from models.doctor import Doctor

def display_welcome_and_instructions():
    print("\nWelcome to the Patient Tracking App")

    print("\nPlease select an option:")

    print("\n1- view doctors' information")
    
    print("\n2- Update doctor information")
    
    print("\n3- Add a new doctor")
    
    print("\n4- View patients' information")
    
    print("\n5- Update patient information")
    
    print("\n6- Add a new patient")
    
    print("\n7- Delete a doctor")
    
    print("\n8- Delete a patient")
    
    print("\n9- Exit")

    print("\nEnter your choice number: ")

def patients_list():
    print("Patients Information")
    patients = Patient.get_all()
    if patients:
        for patient in patients:
           print(f'*** {patient.name} {patient.lastname}, age: {patient.age}')
           print(f'*** Health problem: {patient.disease}')

           doctor = Doctor.get_by_id(patient.doctor_id)
           if doctor:
               print(f'*** Physician: {doctor.name} {doctor.lastname}')
           else:
               print('*** Physician information not found.')
    else:
        print('*** No patients found')
               
           

