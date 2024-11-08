
# helpers.py


from models.patient import Patient
from models.doctor import Doctor

  
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
       print(f'    Health problem: {patient_disease}\n')
       doctor = Doctor.find_by_id(patient_doctor_id)
       if doctor:
           print(f'    Physition: {doctor.name} {doctor.lastname} added.\n')
       else:
           print('*** Physician information not found.\n')
    except ValueError as e:
        print(f"Error: {e}. Please try again.\n")

def delete_patient(patient):
    """Deletes a specified patient after confirmation."""
    confirm = input(f'Are you sure you want to delete {patient.name} {patient.lastname}? (Y/N): ').lower()
    if confirm == 'y':
        patient.delete()
        print(f'*** Success: Patient {patient.name} {patient.lastname} has been deleted.\n')
    elif confirm == 'n':
        print('Deletion canceled.\n')
    else:
        print('Invalid input. Deletion canceled.\n')

def update_patient(patient_id):
   
    patient = Patient.find_by_id(patient_id)
    if not patient:
        print('\n    No patient found.\n')
        return
   
    try:
        name = input(f"\nUpdate patient's name ({patient.name}): ") or patient.name
        patient.name = name
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        lastname = input(f"Update patient's last name ({patient.lastname}): ") or patient.lastname
        patient.lastname = lastname
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        age_input = input(f"Update patient's age ({patient.age}): ")
        age = int(age_input) if age_input else patient.age
        patient.age = age
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        disease = input(f"Update patient's disease ({patient.disease}): ") or patient.disease
        patient.disease = disease
    except ValueError as e:
        print(f"Error: {e}")
       
        
    patient.update()

    print(f'\n**** Success: Patient {patient.name} {patient.lastname}, age: {patient.age}\n')
    print(f'\n    Health condition: {patient.disease}')
    if patient.doctor_id:
        doctor = Doctor.find_by_id(patient.doctor_id)
        if doctor:
            try:
                d_name = input(f"Update doctor's name ({doctor.name}): ") or doctor.name
                doctor.name = d_name
            except ValueError as e:
                print(f"Error: {e}")
            
            try:
                d_lastname = input(f"Update doctor's last name ({doctor.lastname}): ") or doctor.lastname
                doctor.lastname = d_lastname
            except ValueError as e:
                print(f"Error: {e}")
            
            try:
                d_specialty = input(f"Update doctor's specialty ({doctor.specialty}): ") or doctor.specialty
                doctor.specialty = d_specialty
            except ValueError as e:
                print(f"Error: {e}")

            doctor.update()
            print(f'Doctor updated: {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty}')
        else:
            print('\n    Doctor not found.')

    
def doctors_list():
    print("doctors Information\n")
    doctors = Doctor.get_all()
    if doctors:
        for doctor in doctors:
           print(f'*** {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty}\n')
          
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

def get_a_doctor_patients():
    pass

      

# PYTHONPATH=. python -m utils.cli

  

