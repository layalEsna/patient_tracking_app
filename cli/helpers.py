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

def add_patient():
    print('Add New Patient...')
    patient_first_name = input("Enter patient's first name: ")
    patient_lastname = input("Enter patient's last name: ")
    patient_age = input("Enter patient's age: ")
    patient_disease = input("Enter patient's disease: ")
    patient_doctor_id = input("Enter patient's doctor_id: ")
    try:
       Patient.create(patient_first_name, patient_lastname,patient_age, patient_disease, patient_doctor_id)
 
       print(f'*** {patient_first_name} {patient_lastname}, age: {patient_age}')
       print(f'*** Health problem: {patient_disease}')
       doctor = Doctor.find_by_id(patient_doctor_id)
       if doctor:
           print(f'*** Physition: {doctor.name} {doctor.lastname}')
       else:
           print('*** Physician information not found.')
    except ValueError as e:
        print(f"Error: {e}. Please try again.")

def update_patient():
    print('Update Patient...')
    patient_id = input("Enter patient ID.")
    patient = Patient.find_by_id(patient_id)
    if patient:
        patient_first_name = input("Enter patient's first name: ")
        patient_lastname = input("Enter patient's last name: ")
        patient_age = input("Enter patient's age: ")
        patient_disease = input("Enter patient's disease: ")
        patient_doctor_id = input("Enter patient's doctor ID: ")
        try:
            patient.update(patient_first_name, patient_lastname, patient_age, patient_disease, patient_doctor_id)
            print(f'\nUpdated Patient Information:')
            print(f'*** {patient_first_name} {patient_lastname}, age: {patient_age}')
            print(f'*** Health problem: {patient_disease}')
            doctor = Doctor.find_by_id(patient_doctor_id)
            if doctor:
                print(f'*** Physition: {doctor.name} {doctor.lastname}')
            else:
                print('Physician information not found.')
        except ValueError as e:
            print(f'Error: {e}. Please try again.')
    else:
        print('Patient not found')

def delete_patient():
    print('Delete Patient...')
    patient_id = input("Enter patient's ID: ")
    patient = Patient.find_by_id(patient_id)
    if patient:
        confirm = input(f'Are you sure you want to delete {patient.name} {patient.lastname} with ID: {patient_id}? (Y/N): ')
        if confirm.lower() == 'y':
            patient.delete(patient_id)
            print(f'*** Success: Patient {patient.name} {patient.lastname} with ID {patient_id} has been deleted.')
        elif confirm.lower() == 'n':
            print('Deletion canceled.')
        else:
            print('Invalid input. Deletion canceled.')
    else:
        print('Patient not found.')

       




  







               
           
