
# helpers.py


from models.patient import Patient
from models.doctor import Doctor

# from ..models.patient import Patient 
# from ..models.doctor import Doctor

# def display_welcome_and_instructions():
#     print("Welcome to the Patient Tracking App")

#     print("Please select an option:")

#     print("1- view doctors' information\n")
    
#     print("2- Update doctor information\n")
    
#     print("3- Add a new doctor")
    
#     print("4- View patients' information")
    
#     print("5- Update patient information")
    
#     print("6- Add a new patient")
    
#     print("7- Delete a doctor")
    
#     print("8- Delete a patient")
    
#     print("9- Exit")

#     print("Enter your choice number: ")

def patients_list():
    print("Patients Information\n")
    patients = Patient.get_all()
    if patients:
        for patient in patients:
           print(f'*** {patient.name} {patient.lastname}, with ID: {patient.id} age: {patient.age}\n')
           print(f'Health problem: {patient.disease}\n')

           doctor = Doctor.find_by_id(patient.doctor_id)
           if doctor:
               print(f'Physician: {doctor.name} {doctor.lastname}\n')
            #    print('____________________\n')
           else:
               print('*** Physician information not found.\n')
    else:
        print('*** No patients found\n')

def add_patient():
    print('Add New Patient...\n')
    patient_first_name = input("Enter patient's first name: \n")
    patient_lastname = input("Enter patient's last name: \n")
    patient_age = int(input("Enter patient's age: \n"))
    patient_disease = input("Enter patient's disease: \n")
    patient_doctor_id = int(input("Enter patient's doctor_id: \n"))
    try:
       Patient.create(patient_first_name, patient_lastname,patient_age, patient_disease, patient_doctor_id)
 
       print(f'*** Success {patient_first_name} {patient_lastname}, age: {patient_age}\n')
       print(f'Health problem: {patient_disease}\n')
       doctor = Doctor.find_by_id(patient_doctor_id)
       if doctor:
           print(f'Physition: {doctor.name} {doctor.lastname} added.\n')
       else:
           print('*** Physician information not found.\n')
    except ValueError as e:
        print(f"Error: {e}. Please try again.\n")

def update_patient():
    print('Update Patient...\n')
    patient_id = input("Enter patient ID: \n")
    patient = Patient.find_by_id(patient_id)
    if patient:
        patient_first_name = input("Enter patient's first name: \n")
        patient_lastname = input("Enter patient's last name: \n")
        patient_age = int(input("Enter patient's age: \n"))
        patient_disease = input("Enter patient's disease: \n")
        patient_doctor_id = int(input("Enter patient's doctor ID: \n"))
        try:
            patient.update(patient_first_name, patient_lastname, patient_age, patient_disease, patient_doctor_id)
            print(f'\nUpdated Patient Information:\n')
            print(f'*** Success {patient_first_name} {patient_lastname}, age: {patient_age} updated.\n')
            print(f'***  Success Health problem: {patient_disease} updated.\n')
            doctor = Doctor.find_by_id(patient_doctor_id)
            if doctor:
                print(f'***  Success Physition: {doctor.name} {doctor.lastname} Updated.\n')
            else:
                print('Physician information not found.\n')
        except ValueError as e:
            print(f'Error: {e}. Please try again.\n')
    else:
        print('Patient not found\n')

def delete_patient():
    print('Delete Patient...\n')
    patient_id = input("Enter patient's ID: \n")
    patient = Patient.find_by_id(patient_id)
    if patient:
        confirm = input(f'Are you sure you want to delete {patient.name} {patient.lastname} with ID: {patient_id}? (Y/N): \n')
        if confirm.lower() == 'y':
            patient.delete(patient_id)
            print(f'*** Success: Patient {patient.name} {patient.lastname} with ID {patient_id} has been deleted.\n')
        elif confirm.lower() == 'n':
            print('Deletion canceled.\n')
        else:
            print('Invalid input. Deletion canceled.\n')
    else:
        print('Patient not found.\n')

def doctors_list():
    print("doctors Information\n")
    doctors = Doctor.get_all()
    if doctors:
        for doctor in doctors:
           print(f'*** {doctor.name} {doctor.lastname}, with ID: {doctor.id} Specialty: {doctor.specialty}\n')
          
    else:
        print('*** No doctors found\n')

def add_doctor():
    print('Add New doctor...\n')
    doctor_first_name = input("Enter doctor's first name: \n")
    doctor_lastname = input("Enter doctor's last name: \n")
    doctor_specialty = input("Enter doctor's specialty: \n")
    
    try:
       Doctor.create(doctor_first_name, doctor_lastname,doctor_specialty)
       print(f'*** Success {doctor_first_name} {doctor_lastname}, Specialty: {doctor_specialty} added.\n')
       
    except ValueError as e:
        print(f"Error: {e}. Please try again.\n")


def update_doctor():
    print('Update doctor...\n')
    doctor_id = input("Enter doctor ID: \n")
    doctor = Doctor.find_by_id(doctor_id)
    if doctor:
        doctor_first_name = input("Enter doctor's first name: \n")
        doctor_lastname = input("Enter doctor's last name: \n")
        doctor_specialty = input("Enter doctor's specialty: \n")
        try:
            doctor.update(doctor_first_name, doctor_lastname, doctor_specialty)
            print(f'\nUpdated doctor Information:\n')
            print(f'*** Success {doctor_first_name} {doctor_lastname}, Specialty: {doctor_specialty} updated.\n')
           
        except ValueError as e:
            print(f'Error: {e}. Please try again.\n')
    else:
        print('doctor not found\n')

def delete_doctor():
    print('Delete doctor...\n')
    doctor_id = input("Enter doctor's ID: \n")
    doctor = Doctor.find_by_id(doctor_id)
    if doctor:
        confirm = input(f'Are you sure you want to delete {doctor.name} {doctor.lastname} with ID: {doctor_id}? (Y/N): \n')
        if confirm.lower() == 'y':
            doctor.delete(doctor_id)
            print(f'*** Success: doctor {doctor.name} {doctor.lastname} with ID {doctor_id} has been deleted.\n')
        elif confirm.lower() == 'n':
            print('Deletion canceled.\n')
        else:
            print('Invalid input. Deletion canceled.\n')
    else:
        print('doctor not found.\n')

      



  

