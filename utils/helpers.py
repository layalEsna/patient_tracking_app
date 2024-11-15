
# helpers.py   Enter doctor's first name



from models.patient import Patient
from models.doctor import Doctor

def add_patient():
    print('\n    Add New Patient...')
    
    
    patient_first_name = input("\n    Enter patient's first name: ")
    patient_lastname = input("\n    Enter patient's last name: ")
    patient_age = int(input("\n    Enter patient's age: "))
    patient_disease = input("\n    Enter patient's disease: ")


    doctor_name = input("\n    Enter the doctor's first name: ")
    doctor_lastname = input("\n    Enter the doctor's last name: ")
    doctor_specialty = input("\n    Enter the doctor's specialty: ")
    
    doctor = Doctor.get_by_name(doctor_name, doctor_lastname)
    if not doctor:
      
        doctor = Doctor.create(doctor_name, doctor_lastname, doctor_specialty)
        print('\n    ********************')
        print(f'\n    Success: New Physician: {doctor.name} {doctor.lastname} Specialty: {doctor.specialty} added.')
        print('\n    ********************')
    else:
        print('\n    ********************')
        print(f'\n    Physician: {doctor.name} {doctor.lastname} found and assigned to the patient.')
        print('\n    ********************')
 
    new_patient = Patient.create(
        name=patient_first_name,
        lastname=patient_lastname,
        age=patient_age,
        disease=patient_disease,
        doctor_id=doctor.id
    )



    if new_patient:
        print('\n      ********************')
        print(f'\n      Success: New Patient: {new_patient.name} {new_patient.lastname}, age: {new_patient.age}, Health Condition: {new_patient.disease}')
        print(f'\n      Assigned Physician: {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty}')
        print('\n      ********************')
    else:
        print('\n    Failed to create the new patient.')

def delete_patient(patient):
    """Deletes a specified patient after confirmation."""
    confirm = input(f'    Are you sure you want to delete {patient.name} {patient.lastname}? (Y/N): ').lower()
    if confirm == 'y':
        patient.delete()
        print('\n      ********************')
        print(f'\n     Success: Patient {patient.name} {patient.lastname} has been deleted.')
        print('\n      ********************')
    elif confirm == 'n':
        print('\n      ********************')
        print('\n    Deletion canceled.\n')
        print('\n      ********************')
    else:
        print('\n      ********************')
        print('\n    Invalid input. Deletion canceled.')
        print('\n      ********************')

       

def update_patient(patient_id):
    print('\n    Update Patient...')

    patient = Patient.find_by_id(patient_id)
    if patient:
        
        try:
            patient_first_name = input(f"\n    Update patient's first name ({patient.name}):  ") or patient.name
            patient.name = patient_first_name  
        except ValueError as e:
            print(f"\n    Error in first name: {e}")
            return  
     
        
        try:
            patient_lastname = input(f"\n    Update patient's last name ({patient.lastname}):  ") or patient.lastname
            patient.lastname = patient_lastname  
        except ValueError as e:
            print(f"\n    Error in last name: {e}")
            return  
        
       
        try:
            patient_age_input = input(f"\n    Update patient's age ({patient.age}):  ") or str(patient.age)
            if patient_age_input.isdigit():
                patient.age = int(patient_age_input) 
            else:
                raise ValueError('\n    Age must be an integer between 18 and 100.')
        except ValueError as e:
            print(f"\n    Error in age: {e}")
            return  
        
        
        try:
            patient_disease = input(f"\n    Update patient's disease ({patient.disease}):  ") or patient.disease
            patient.disease = patient_disease  
        except ValueError as e:
            print(f"\n    Error in disease: {e}")
            return  

        
        try:
            patient.update()

            # print('      ********************')
            # print(f'\n    Success patient updated: {patient.name} {patient.lastname}, age: {patient.age}')
            # print(f'\n    Health condition: {patient.disease}')
            # print('\n      ********************')

        except ValueError as e:
            print(f'\n    Error: {e}. Please try again.')

        
        if patient.doctor_id:
            doctor = Doctor.find_by_id(patient.doctor_id)
            if doctor:
                try:
                    doctor_name = input(f"\n    Update doctor's name ({doctor.name}): ") or doctor.name
                    doctor.name = doctor_name  
                except ValueError as e:
                    print(f"\n    Error in doctor's name: {e}")
                    return  

                try:
                    doctor_lastname = input(f"\n    Update doctor's last name ({doctor.lastname}): ") or doctor.lastname
                    doctor.lastname = doctor_lastname  
                except ValueError as e:
                    print(f"    Error in doctor's last name: {e}\n")
                    return  

                try:
                    doctor_specialty = input(f"\n    Update doctor's specialty ({doctor.specialty}): ") or doctor.specialty
                    doctor.specialty = doctor_specialty  
                except ValueError as e:
                    print(f"Error in doctor's specialty: {e}")
                    return  

                try:
                    doctor.update()

                    # print('\n      ********************')


                    print('\n      ********************')
                    print(f'\n    Success patient updated: {patient.name} {patient.lastname}, age: {patient.age}')
                    print(f'\n    Health condition: {patient.disease}')
                    # print('\n      ********************')

                    print(f'\n    Success: Physician: {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty} updated for patient {patient.name} {patient.lastname}')
                    print('\n      ********************')

                except ValueError as e:
                    print(f'\n    Error: {e}. Please try again.')
            else:
                print('\n    No doctor found for this patient.')

    else:
        print(f'\n    Patient not found.')


def add_doctor():
    print('\n    Add New doctor...')
    doctor_first_name = input("\n    Enter doctor's first name: ")
    doctor_lastname = input("\n    Enter doctor's last name: ")
    doctor_specialty = input("\n    Enter doctor's specialty: ")
    
    try:
       Doctor.create(doctor_first_name, doctor_lastname,doctor_specialty)
       print('\n    ********************')
       print(f'\n     Success {doctor_first_name} {doctor_lastname}, Specialty: {doctor_specialty} added.')
       print('\n    ********************')
       
    except ValueError as e:
        print(f"\n    Error: {e}. Please try again.")


def update_doctor(doctor):
    print('\n    Update Doctor...')
    
    doctor = Doctor.find_by_id(doctor.id)
    
   
    if doctor:
        doctor_first_name = input(f"(\n    Enter doctor's name: {doctor.name}) ") or doctor.name
        doctor_lastname = input(f"(\n    Enter doctor's last name: {doctor.lastname}) ") or doctor.lastname
        doctor_specialty = input(f"(\n    Enter doctor's name: {doctor.specialty}) ") or doctor.specialty

        try:
            doctor.update(doctor_first_name, doctor_lastname, doctor_specialty)
           
            print('\n    ********************')
            print(f'\n     Success {doctor_first_name} {doctor_lastname}, Specialty: {doctor_specialty} updated.')
            print('\n    ********************')
        except ValueError as e:
            print(f'\n    Error: {e}. Please try again.\n')
    else:
        print('\n    doctor not found')

def delete_doctor(doctor):
    print('\n    Delete doctor...')
    
    doctor = Doctor.find_by_id(doctor.id)
    if doctor:
        confirm = input(f'\n    Are you sure you want to delete {doctor.name} {doctor.lastname}? (y/n): ')
        if confirm.lower() == 'y':
            Doctor.delete(doctor.id)
            print('\n    *******************')
            print(f'\n     Success: doctor {doctor.name} {doctor.lastname} has been deleted.')
            print('\n    *******************')
        elif confirm.lower() == 'n':
            print('\n        ********************')
            print('\n    Deletion canceled.')
            print('\n    *******************')
        else:
            print('\n    Invalid input. Deletion canceled.')
    else:
        print('\n    Doctor not found.')
        

def get_a_doctor_patients(doctor):
    doctor = Doctor.get_by_name(doctor.name, doctor.lastname)
    if doctor:
        patients = doctor.list_a_doctor_patients()
        if patients:
            print('\n      ********************')
            print(f'\n      List of patients for Dr. {doctor.name} {doctor.lastname}')
            for i, patient in enumerate(patients, start=1):
                print(f'\n    {i}- {patient.name} {patient.lastname}')
               
            return patients 
        
        else:
             print('\n    ********************')
             print(f'\n    No patients found for Dr. {doctor.name} {doctor.lastname}.')
             print('\n    ********************')

      

 # PYTHONPATH=. python -m utils.cli    



