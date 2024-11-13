
# helpers.py


from models.patient import Patient
from models.doctor import Doctor

def add_patient():
    print('\n    Add New Patient...\n')
    
   
    patient_first_name = input("\n    Enter patient's first name: \n")
    patient_lastname = input("\n    Enter patient's last name: \n")
    patient_age = int(input("\n    Enter patient's age: \n"))
    patient_disease = input("Enter patient's disease: \n")


    doctor_name = input("\n    Enter the doctor's first name: \n")
    doctor_lastname = input("\n    Enter the doctor's last name: \n")
    
    
    doctor = Doctor.get_by_name(doctor_name, doctor_lastname)
    if not doctor:
        doctor_specialty = input("\n    Enter the doctor's specialty: \n")
        doctor = Doctor.create(doctor_name, doctor_lastname, doctor_specialty)
        print(f'\n    New Physician: {doctor.name} {doctor.lastname} added with specialty: {doctor.specialty}.')
    else:
        print(f'\n    Physician: {doctor.name} {doctor.lastname} found and assigned to the patient.')

 
    new_patient = Patient.create(
        name=patient_first_name,
        lastname=patient_lastname,
        age=patient_age,
        disease=patient_disease,
        doctor_id=doctor.id
    )

   
    if new_patient:
        print('\n      ********************')
        print(f'\n     Success: New Patient: {new_patient.name} {new_patient.lastname}, age: {new_patient.age}, Health Condition: {new_patient.disease}')
        print(f'       Assigned Physician: {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty}')
        print('\n      ********************')
    else:
        print('\n    Failed to create the new patient.')

def delete_patient(patient):
    """Deletes a specified patient after confirmation."""
    confirm = input(f'    Are you sure you want to delete {patient.name} {patient.lastname}? (Y/N): ').lower()
    if confirm == 'y':
        patient.delete()
        print('      ********************\n')
        print(f'    \n*** Success: Patient {patient.name} {patient.lastname} has been deleted.\n')
    elif confirm == 'n':
        print('\n    Deletion canceled.\n')
    else:
        print('\n    Invalid input. Deletion canceled.\n')
        print('      ********************\n')

       

def update_patient(patient_id):
    print('\n    Update Patient...\n')

    patient = Patient.find_by_id(patient_id)
    if patient:
        
        try:
            patient_first_name = input(f"\n    Update patient's first name ({patient.name}):  ") or patient.name
            patient.name = patient_first_name  
        except ValueError as e:
            print(f"Error in first name: {e}")
            return  
        
        
        try:
            patient_lastname = input(f"\n    Update patient's last name ({patient.lastname}):  ") or patient.lastname
            patient.lastname = patient_lastname  
        except ValueError as e:
            print(f"Error in last name: {e}")
            return  
        
       
        try:
            patient_age_input = input(f"\n    Update patient's age ({patient.age}):  ") or str(patient.age)
            if patient_age_input.isdigit():
                patient.age = int(patient_age_input) 
            else:
                raise ValueError('Age must be an integer between 18 and 100.')
        except ValueError as e:
            print(f"Error in age: {e}")
            return  
        
        
        try:
            patient_disease = input(f"\n    Update patient's disease ({patient.disease}):  ") or patient.disease
            patient.disease = patient_disease  
        except ValueError as e:
            print(f"Error in disease: {e}")
            return  

        
        try:
            patient.update()

            print('      ********************')
            print(f'\n    Success patient updated: {patient.name} {patient.lastname}, age: {patient.age}\n')
            print(f'\n    Health condition: {patient.disease}\n')
            print('      ********************')

        except ValueError as e:
            print(f'\n    Error: {e}. Please try again.\n')

        
        if patient.doctor_id:
            doctor = Doctor.find_by_id(patient.doctor_id)
            if doctor:
                try:
                    doctor_name = input(f"\n    Update doctor's name ({doctor.name}): ") or doctor.name
                    doctor.name = doctor_name  
                except ValueError as e:
                    print(f"Error in doctor's name: {e}")
                    return  

                try:
                    doctor_lastname = input(f"\n    Update doctor's last name ({doctor.lastname}): ") or doctor.lastname
                    doctor.lastname = doctor_lastname  
                except ValueError as e:
                    print(f"Error in doctor's last name: {e}")
                    return  

                try:
                    doctor_specialty = input(f"\n    Update doctor's specialty ({doctor.specialty}): ") or doctor.specialty
                    doctor.specialty = doctor_specialty  
                except ValueError as e:
                    print(f"Error in doctor's specialty: {e}")
                    return  

                try:
                    doctor.update()

                    print('      ********************')
                    print(f'\n    Physician: {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty}\n')
                    print('      ********************\n')

                except ValueError as e:
                    print(f'\n    Error: {e}. Please try again.\n')
            else:
                print('\n No doctor found for this patient.')

    else:
        print(f'\n    Patient not found.')


def add_doctor():
    print('\n    Add New doctor...\n')
    doctor_first_name = input("\n    Enter doctor's first name: ")
    doctor_lastname = input("\n    Enter doctor's last name: ")
    doctor_specialty = input("\n    Enter doctor's specialty: ")
    
    try:
       Doctor.create(doctor_first_name, doctor_lastname,doctor_specialty)
       print('\n    ********************\n')
       print(f'\n     Success {doctor_first_name} {doctor_lastname}, Specialty: {doctor_specialty} added.\n')
       print('\n    ********************\n')
       
    except ValueError as e:
        print(f"\n    Error: {e}. Please try again.\n")


def update_doctor(doctor):
    print('\n    Update Doctor...\n')
    
    
    # doctor = Doctor.find_by_id(doctor.id)
    if doctor:
        
        doctor_first_name = input(f"\n    Update doctor's first name ({doctor.name}):  ") or doctor.name
        doctor_lastname = input(f"\n    Update doctor's last name ({doctor.lastname}):  ") or doctor.lastname
        doctor_specialty = input(f"\n    Update doctor's specialty ({doctor.specialty}):  ") or doctor.specialty
        try:
            doctor.update(doctor_first_name, doctor_lastname, doctor_specialty)
           
            print('\n    ********************')
            print(f'\n     Success {doctor_first_name} {doctor_lastname}, Specialty: {doctor_specialty} updated.\n')
            print('    ********************')
        except ValueError as e:
            print(f'\n    Error: {e}. Please try again.\n')
    else:
        print('\n    doctor not found\n')

def delete_doctor(doctor):
    print('\n    Delete doctor...\n')
    
    doctor = Doctor.find_by_id(doctor.id)
    if doctor:
        confirm = input(f'\n    Are you sure you want to delete {doctor.name} {doctor.lastname}? (y/n): ')
        if confirm.lower() == 'y':
            Doctor.delete(doctor.id)
            print('    *******************\n')
            print(f'\n     Success: doctor {doctor.name} {doctor.lastname} has been deleted.\n')
            print('    *******************\n')
        elif confirm.lower() == 'n':
            print('        ********************\n')
            print('\n    Deletion canceled.\n')
            print('    *******************\n')
        else:
            print('\n    Invalid input. Deletion canceled.\n')
    else:
        print('\n    Doctor not found.\n')
        

def get_a_doctor_patients(doctor):
    doctor = Doctor.get_by_name(doctor.name, doctor.lastname)
    if doctor:
        patients = doctor.list_a_doctor_patients()
        if patients:
            print('\n      ********************')
            print(f'\n      List of patients for Dr. {doctor.name} {doctor.lastname}\n')
            for i, patient in enumerate(patients, start=1):
                print(f'\n    {i}- {patient.name} {patient.lastname}\n')
                print('        ********************\n')
            return patients 
        else:
             print(f'    No patients found for {doctor.name} {doctor.lastname}.\n')
    

      

 # PYTHONPATH=. python -m utils.cli



