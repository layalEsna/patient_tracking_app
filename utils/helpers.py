
# helpers.py


from models.patient import Patient
from models.doctor import Doctor


    

#     print('\n    Add New Patient...\n')
#     # patient_doctor_id
    
#     patient_first_name = input("\n    Enter patient's first name: \n")
#     patient_lastname = input("\n    Enter patient's last name: \n")
#     patient_age = int(input("\n    Enter patient's age: \n"))
#     patient_disease = input("\n    Enter patient's disease: \n")

#     patient_doctor_id = None


#     doctor_name = input("\n    Enter the doctor's first name: \n")
#     doctor_lastname = input("\n    Enter the doctor's last name: \n")
        
#     # print(f'\n    *** Success: New Patient: {patient_first_name} {patient_lastname}, age: {patient_age}, Disease: {patient_disease}\n')

#     # Try to fetch the doctor by name
#     doctor = Doctor.get_by_name(doctor_name, doctor_lastname)

#     if doctor:
#         # If the doctor exists, assign their ID to the patient
#         patient_doctor_id = doctor.id
#         # print(f'\n    Physician: {doctor_name} {doctor_lastname} found and assigned to the patient.')
#     else:
#         # If no doctor is found, create a new one
#         print(f'\n    No doctor found with name: {doctor_name} {doctor_lastname}.\n')
#         doctor_specialty = input("\n    Enter the doctor's specialty: \n")
        
#         # Create the new doctor
#         doctor = Doctor.create(doctor_name, doctor_lastname, doctor_specialty)
#         patient_doctor_id = doctor.id
#         print(f'\n    New Physician: {doctor_name} {doctor_lastname} added.')

#     # Create the new patient and associate with the doctor
#     new_patient = Patient.create(patient_first_name, patient_lastname, patient_age, patient_disease, doctor_id=patient_doctor_id)

#     # Print out the new patient details for confirmation
#     if new_patient:
#         print(f'\n    *** Success: New Patient: {new_patient.name} {new_patient.lastname}, age: {new_patient.age}, Health Condition: {new_patient.disease}')
#         print(f'       Physician: {doctor_name} {doctor_lastname}')
#     else:
#         print('\n    Failed to create the new patient.')

# def add_patient():
#     print('\n    Add New Patient...\n')
    
#     # Get patient details
#     patient_first_name = input("\n    Enter patient's first name: \n")
#     patient_lastname = input("\n    Enter patient's last name: \n")
#     patient_age = int(input("\n    Enter patient's age: \n"))
#     patient_disease = input("Enter patient's disease: \n")

#     # Initialize doctor details
#     doctor_name = input("\n    Enter the doctor's first name: \n")
#     doctor_lastname = input("\n    Enter the doctor's last name: \n")
    
#     # Attempt to retrieve the doctor by name and last name
#     doctor = Doctor.get_by_name(doctor_name, doctor_lastname)
    
#     # If the doctor does not exist, prompt for specialty and create a new one
#     if not doctor:
#         print(f'\n    No doctor found with name: {doctor_name} {doctor_lastname}.\n')
#         doctor_specialty = input("\n    Enter the doctor's specialty: \n")
#         doctor = Doctor.create(doctor_name, doctor_lastname, doctor_specialty)
#         print(f'\n    New Physician: {doctor.name} {doctor.lastname} added with specialty: {doctor.specialty}.')
#     else:
#         print(f'\n    Physician: {doctor.name} {doctor.lastname} found and assigned to the patient.')

#     # Now create the patient with the doctor’s ID
#     new_patient = Patient.create(patient_first_name, patient_lastname, patient_age, patient_disease, doctor_id=doctor.id)

#     # Confirm the new patient’s details
#     if new_patient:
#         print(f'\n    *** Success: New Patient: {new_patient.name} {new_patient.lastname}, age: {new_patient.age}, Health Condition: {new_patient.disease}')
#         print(f'       Assigned Physician: {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty}')
#     else:
#         print('\n    Failed to create the new patient.')

def add_patient():
    print('\n    Add New Patient...\n')
    
    # Get patient details
    patient_first_name = input("\n    Enter patient's first name: \n")
    patient_lastname = input("\n    Enter patient's last name: \n")
    patient_age = int(input("\n    Enter patient's age: \n"))
    patient_disease = input("Enter patient's disease: \n")

    # Get doctor details
    doctor_name = input("\n    Enter the doctor's first name: \n")
    doctor_lastname = input("\n    Enter the doctor's last name: \n")
    
    # Retrieve or create doctor
    doctor = Doctor.get_by_name(doctor_name, doctor_lastname)
    if not doctor:
        doctor_specialty = input("\n    Enter the doctor's specialty: \n")
        doctor = Doctor.create(doctor_name, doctor_lastname, doctor_specialty)
        print(f'\n    New Physician: {doctor.name} {doctor.lastname} added with specialty: {doctor.specialty}.')
    else:
        print(f'\n    Physician: {doctor.name} {doctor.lastname} found and assigned to the patient.')

    # Create the new patient with doctor’s ID
    new_patient = Patient.create(
        name=patient_first_name,
        lastname=patient_lastname,
        age=patient_age,
        disease=patient_disease,
        doctor_id=doctor.id
    )

    # Confirm patient details
    if new_patient:
        print(f'\n    *** Success: New Patient: {new_patient.name} {new_patient.lastname}, age: {new_patient.age}, Health Condition: {new_patient.disease}')
        print(f'       Assigned Physician: {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty}')
    else:
        print('\n    Failed to create the new patient.')

def delete_patient(patient):
    """Deletes a specified patient after confirmation."""
    confirm = input(f'    Are you sure you want to delete {patient.name} {patient.lastname}? (Y/N): ').lower()
    if confirm == 'y':
        patient.delete()
        print(f'    \n*** Success: Patient {patient.name} {patient.lastname} has been deleted.\n')
    elif confirm == 'n':
        print('\n    Deletion canceled.\n')
    else:
        print('\n    Invalid input. Deletion canceled.\n')

def update_patient(patient_id):
    print('\n    Update patient...\n')
    patient = Patient.find_by_id(patient_id)
    if not patient:
        print('\n    No patient found.\n')
        return
   
    try:
        name = input(f"\n    Update patient's name ({patient.name}): ") or patient.name
        patient.name = name
    except ValueError as e:
        print(f"    Error: {e}")
    
    try:
        lastname = input(f"\n    Update patient's last name ({patient.lastname}): ") or patient.lastname
        patient.lastname = lastname
    except ValueError as e:
        print(f"    Error: {e}")
    
    try:
        age_input = input(f"\n    Update patient's age ({patient.age}): ")
        age = int(age_input) if age_input else patient.age
        patient.age = age
    except ValueError as e:
        print(f"    Error: {e}")
    
    try:
        disease = input(f"\n    Update patient's disease ({patient.disease}): ") or patient.disease
        patient.disease = disease
    except ValueError as e:
        print(f"\n    Error: {e}")
       
        
    patient.update()

    if patient.doctor_id:

        doctor = Doctor.find_by_id(patient.doctor_id)
        if doctor:
            try:
                d_name = input(f"\n    Update doctor's name ({doctor.name}): ") or doctor.name
                doctor.name = d_name
            except ValueError as e:
                print(f"Error: {e}")
            
            try:
                d_lastname = input(f"\n    Update doctor's last name ({doctor.lastname}): ") or doctor.lastname
                doctor.lastname = d_lastname
            except ValueError as e:
                print(f"Error: {e}")
            
            try:
                d_specialty = input(f"\n    Update doctor's specialty ({doctor.specialty}): ") or doctor.specialty


                doctor.specialty = d_specialty

                print(f'\n    **** Success patient updated: {patient.name} {patient.lastname}, age: {patient.age}\n')
                print(f'\n    Health condition: {patient.disease}\n')

            except ValueError as e:
                print(f"\n    Error: {e}")

            doctor.update()
            print(f'\n    **** Success doctor updated: {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty}\n')
        else:
            print('\n    Doctor not found.\n')

    
def doctors_list():
    print("\n    doctors Information\n")
    doctors = Doctor.get_all()
    if doctors:
        for doctor in doctors:
           print(f'\n    *** {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty}\n')
          
    else:
        print('\n    *** No doctors found\n')

def add_doctor():
    print('\n    Add New doctor...\n')
    doctor_first_name = input("\n    Enter doctor's first name: \n")
    doctor_lastname = input("\n    Enter doctor's last name: \n")
    doctor_specialty = input("\n    Enter doctor's specialty: \n")
    
    try:
       Doctor.create(doctor_first_name, doctor_lastname,doctor_specialty)
       print(f'\n    *** Success {doctor_first_name} {doctor_lastname}, Specialty: {doctor_specialty} added.\n')
       
    except ValueError as e:
        print(f"\n    Error: {e}. Please try again.\n")


def update_doctor(doctor):
    print('\n    Update doctor...\n')
    # doctor_id = input("Enter doctor ID: \n")
    
    doctor = Doctor.find_by_id(doctor.id)
    if doctor:
        row = doctor
        print (row)
        doctor_first_name = input(f"\n    Update doctor's first name ({doctor.name}):  ") or doctor.name
        doctor_lastname = input(f"\n    Update doctor's last name ({doctor.lastname}):  ") or doctor.lastname
        doctor_specialty = input(f"\n    Update doctor's specialty ({doctor.specialty}):  ") or doctor.specialty
        try:
            doctor.update(doctor_first_name, doctor_lastname, doctor_specialty)
            print(f'\n    Updated doctor Information:\n')
            print(f'\n    *** Success {doctor_first_name} {doctor_lastname}, Specialty: {doctor_specialty} updated.\n')
           
        except ValueError as e:
            print(f'\n    Error: {e}. Please try again.\n')
    else:
        print('\n    doctor not found\n')

def delete_doctor(doctor):
    print('\n    Delete doctor...\n')
    # doctor_id = input("\n    Enter doctor's ID: \n")
    doctor = Doctor.find_by_id(doctor.id)
    if doctor:
        confirm = input(f'\n    Are you sure you want to delete {doctor.name} {doctor.lastname}? (Y/N): ')
        if confirm.lower() == 'y':
            Doctor.delete(doctor.id)
            print(f'\n    *** Success: doctor {doctor.name} {doctor.lastname} has been deleted.\n')
        elif confirm.lower() == 'n':
            print('\n    Deletion canceled.\n')
        else:
            print('\n    Invalid input. Deletion canceled.\n')
    else:
        print('\n    Doctor not found.\n')

def get_a_doctor_patients(self):
    patients = self.list_a_doctor_patients()
    return patients if patients else None
    # doctor = Doctor.find_by_id(doctor_id)
    # if doctor:

    #     patients = doctor.list_a_doctor_patients(doctor_id)
    
    #     return [ patient for patient in patients]
    # else:
    #     return None
    
# Elon hbh, Specialty: kjbhv
      

# PYTHONPATH=. python -m utils.cli

  

