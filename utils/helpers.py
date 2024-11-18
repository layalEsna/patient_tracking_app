
# helpers.py  



from models.patient import Patient
from models.doctor import Doctor


# ----
def add_patient():
    while True:
        try:

            patient_name = input("\n    Enter patient's name: ")
            if not isinstance(patient_name, str) or len(patient_name) < 2:
                print('\n    ********************')
                raise ValueError('\n    Name must be a string and more than 2 characters.')
            print('\n    ********************')
            break
        except ValueError:
            print('\n    ********************')
            print('\n    Name must be a string and more than 2 characters.')
            print('\n    ********************')
    while True:
        try:
            patient_lastname = input("\n    Enter patient's last name: ")
            if not isinstance(patient_lastname, str) or len(patient_lastname) < 2:
                print('\n    ********************')
                raise ValueError('\n    Last name must be a string and more than 2 characters.')
            print('\n    ********************')
            break
        except ValueError:
            print('\n    ********************')
            print('\n    Last name must be a string and more than 2 characters.')
            print('\n    ********************')
    while True:
        try:
            patient_age = int(input("\n    Enter patient's age: "))
            if not (18 <= patient_age <= 100):
                print('\n    ********************')
                raise ValueError('\n    Age must be a number between 18 and 100 inclusive.')
            print('\n    ********************')
            break
        except ValueError:
            print('\n    ********************')
            print('\n    Age must be a number between 18 and 100 inclusive....')
            print('\n    ********************')
        
    while True:
        try:
            disease = input("\n    Enter patient's disease: ")
            if not isinstance(disease, str) or len(disease) < 2:
                print('\n    ********************')
                raise ValueError('\n    Disease must be a string and more than 2 characters.')
            print('\n    ********************')
            break
        except ValueError:
            print('\n    ********************')
            print('\n    Disease must be a string and more than 2 characters.')
            print('\n    ********************')
    while True:
        try:
            doctor_name = input("\n    Enter doctor's name: ") 
            if not isinstance(doctor_name, str) or len(doctor_name) < 2:
                print('\n    ********************')
                raise ValueError('\n    Name must be a string and more than 2 characters.')
            print('\n    ********************')
            break
        except ValueError:
            print('\n    ********************')
            print('\n    Name must be a string and more than 2 characters.')
            print('\n    ********************')
    while True:
        try:
            doctor_lastname = input("\n    Enter doctor's last name: ") 
            if not isinstance(doctor_lastname, str) or len(doctor_lastname) < 2:
                print('\n    ********************')
                raise ValueError('\n     Last name must be a string and more than 2 characters.')
            print('\n    ********************')
            break
        except ValueError:
            print('\n    ********************')
            print('\n     Last name must be a string and more than 2 characters.')
            print('\n    ********************')

    while True:
        try:
            specialty =  input("\n    Enter doctor's specialty: ") 
            if not isinstance(specialty, str) or len(specialty) < 2:
                print('\n    ********************')
                raise ValueError('\n    Specialty must be a string and more than 2 characters.')
            print('\n    ********************')
            break
        except ValueError:
            print('\n    ********************')
            print('\n    Specialty must be a string and more than 2 characters.')
            print('\n    ********************')
    

    doctor = Doctor.get_by_name(doctor_name, doctor_lastname)
    if not doctor:
        doctor = Doctor.create(doctor_name, doctor_lastname, specialty)
        print('\n    ********************')
        print(f'\n    Success: New Doctor: {doctor_name} {doctor_lastname}: Specialty: {specialty} added.')
        print('\n    ********************')

    new_patient = Patient.create(patient_name, patient_lastname, patient_age, disease,doctor.id)
        

    if new_patient:
                    print('\n    ********************')
                    print(f'\n    Success: New Patient: {patient_name} {patient_lastname}, Age {patient_age} Health Condition: {disease} added')
                    print(f'\n    Assigned doctor: Dr. {doctor_name} {doctor_lastname}, Specialty: {specialty}')
                    print('\n    ********************')
           



def delete_patient(patient): 
    
    if patient:

        while True:
            
                confirm = input(f'\n    Are you sure that you want to delet {patient.name} {patient.lastname}? (y/n): ').lower()
                
                if confirm == 'y':
                    patient.delete()
                    print('\n      ********************')
                    print(f'\n     Success: Patient {patient.name} {patient.lastname} has been deleted.')
                    print('\n      ********************')
                    break
                elif confirm == 'n':
                    print('\n      ********************')
                    print('\n    Deletion canceled.')
                    print('\n      ********************') 
                    break

           
                else:
                     print('\n    ********************')
                     print('\n    Invalid input. Please enter "y" for yes or "n" for no.')
                     print('\n    ********************')


 

def update_patient(patient):
    if isinstance(patient, Patient): 
        while True: 
            try:
                patient_name = input(f"\n    Update Patient's name ({patient.name}): ") or patient.name
                if not isinstance(patient_name, str) or len(patient_name) < 2:
                    print('\n    ********************')
                    raise ValueError("\n    Patient's name must be a string and more than 2 characters.")
                print('\n    ********************')
                patient.name = patient_name
                # patient.update()  # Save changes immediately
                break
            except ValueError:
                print('\n    ********************')
                print("\n    Patient's name must be a string and more than 2 characters.")
                print('\n    ********************')
                

        while True:
            try:
                patient_lastname = input(f"\n    Update Patient's lastname ({patient.lastname}): ") or patient.lastname
                if not isinstance(patient_lastname, str) or len(patient_lastname) < 2:
                    print('\n    ********************')
                    raise ValueError("\n    Patient's lastname must be a string and more than 2 characters.")
                print('\n    ********************')
                patient.lastname = patient_lastname
                # patient.update()  # Save changes immediately
                break
            except ValueError:
                print('\n    ********************')
                print("\n    Patient's last name must be a string and more than 2 characters.")
                print('\n    ********************')
        
        while True:
            try:
                age_input = input(f"\n    Update Patient's age ({patient.age}): ")
                if age_input.strip() == '':
                    patient_age = patient.age
                else:
                    patient_age = int(age_input)
                    if not (18 <= patient_age <= 100):
                        print('\n    ********************')
                        raise ValueError("\n    Patient's age must be a number and between 18 and 100 inclusive.")
                    print('\n    ********************')
                patient.age = patient_age
                # patient.update()  # Save changes immediately
                break
            except ValueError:
                print('\n    ********************')
                print("\n    Patient's age must be a number and between 18 and 100 inclusive.")
                print('\n    ********************')
        
        while True:
            try:
                patient_disease = input(f"\n    Update Patient's disease ({patient.disease}): ") or patient.disease
                if not isinstance(patient_disease, str) or len(patient_disease) < 2:
                    print('\n    ********************')
                    raise ValueError("\n    Patient's disease must be a string and more than 2 characters.")
                print('\n    ********************')
                patient.disease = patient_disease
                # patient.update()  # Save changes immediately
                break
            except ValueError:
                print('\n    ********************')
                print("\n    Patient's disease must be a string and more than 2 characters.")
                print('\n    ********************')
        patient.update()
        
        if patient.doctor_id:
            doctor = Doctor.find_by_id(patient.doctor_id)
            if doctor:
                print('\n    ********************')
                print(f'\n    Success: Patient {patient.name} {patient.lastname}, age {patient.age} Health condition: {patient.disease} updated.')
                print(f"\n    Physician: Dr. {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty}")
                print('\n    ********************')
            else:
                while True:
                    try:
                        confirm_add = input(f'\n    Do you want to assign a doctor to {patient.name} {patient.lastname} (y/n)?: ').lower()
                        if confirm_add == 'y':
                            new_doctor = add_doctor()
                            if new_doctor:
                                patient.doctor_id = new_doctor.id
                                patient.update()  
                                print('\n    ********************')
                                print(f'\n    Success: Patient {patient.name} {patient.lastname}, age {patient.age} Health condition: {patient.disease} updated.')
                                print(f"\n    New Physician: Dr. {new_doctor.name} {new_doctor.lastname}, Specialty: {new_doctor.specialty}")
                                print('\n    ********************')
                            else:
                                print("\n    Doctor assignment failed. Please try again.")
                            break
                        elif confirm_add == 'n':
                            print('\n    ********************')
                            print('\n    No doctor assigned.')
                            print('\n    ********************')
                            break
                        else:
                            print('\n    ********************')
                            print('\n    Invalid input. Please enter "y" or "n".')
                            print('\n    ********************')
                    except ValueError:
                        print('\n    ********************')
                        print('\n    No doctor assigned.')
                        print('\n    ********************')
        else:
            print('\n    ********************')
            print(f'\n    Success: Patient {patient.name} {patient.lastname}, age {patient.age} Health condition: {patient.disease} updated.')
            print('\n    ********************')


def add_doctor():
    
    print('\n    Add New doctor...')
    while True:
        try:
            doctor_first_name = input(f"\n    Update doctor's name: ") 
            if not isinstance(doctor_first_name, str) or len(doctor_first_name) < 2:
                raise ValueError("\n    Doctor's name must be a string and more than 2 characters.")
            break
        except ValueError:
            print("\n    Doctor's name must be a string and more than 2 characters.")

    while True:
        try:

            doctor_lastname = input(f"\n    Enter doctor's last name: ") 
            if not isinstance(doctor_lastname, str) or len(doctor_lastname) < 2:
                raise ValueError('\n    Last name must be a string and more than 2 characters.')
            break
        except ValueError:
            print('\n    Last name must be a string and more than 2 characters.')
            break
    

    while True:
        try:

            doctor_specialty = input(f"\n    Enter doctor's pecialty: ") 
            if not isinstance(doctor_specialty, str) or len(doctor_specialty) < 2:
                raise ValueError('\n    Specialty must be a string and more than 2 characters.')
            break
        except ValueError:
            print('\n    Specialty must be a string and more than 2 characters.')
    



    try:
       doctor = Doctor.create(doctor_first_name, doctor_lastname,doctor_specialty)
       print('\n    ********************')
       print(f'\n     Success {doctor_first_name} {doctor_lastname}, Specialty: {doctor_specialty} added.')
       print('\n    ********************')
       return doctor
    except ValueError as e:
        print(f"\n    Error: {e}. Please try again.")
        return None
        
# ------

def update_doctor(doctor):
    if isinstance(doctor, Doctor): 
        while True:
            try:
                doctor_name = input(f"\n    Update doctor's name ({doctor.name}): ") or doctor.name
                if not isinstance(doctor_name, str) or len(doctor_name) < 2:
                    raise ValueError("\n    Doctor's name must be a string and more than 2 characters.")
                doctor.name = doctor_name
                break
            except ValueError:
                print("\n    Doctor's name must be a string and more than 2 characters.")
    
        while True:
            try:
                doctor_lastname = input(f"\n    Update doctor's last name ({doctor.lastname}): ") or doctor.lastname
                if not isinstance(doctor_lastname, str) or len(doctor_lastname) < 2:
                    raise ValueError("\n    Doctor's last name must be a string and more than 2 characters.")
                doctor.lastname = doctor_lastname
                break
            except ValueError:
                print("\n    Doctor's last name must be a string and more than 2 characters.")
            
        while True:
            try:
                doctor_specialty = input(f"\n    Update doctor's specialty ({doctor.specialty}): ") or doctor.specialty
                if not isinstance(doctor_specialty, str) or len(doctor_specialty) < 2:
                    raise ValueError("\n    Doctor's specialty must be a string and more than 2 characters.")
                doctor.specialty = doctor_specialty
                break
            except ValueError:
                print("\n    Doctor's specialty must be a string and more than 2 characters.")

        # Call the update method on the doctor instance
        doctor.update()
        print('\n    ********************')
        print(f'\n    Success: Dr {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty} updated')
        print('\n    ********************')
    else:
        print('\n    Invalid doctor instance.')
     
    

def delete_doctor(doctor):
    # if isinstance(doctor, Doctor):
        while True:
            confirm = input(f'\n    Are you sure that you want to delete Dr. {doctor.name} {doctor.lastname}? (y/n): ').lower()
            if confirm == 'y':
                doctor.delete(doctor.id)
                print('\n    ********************')
                print(f'\n    Success: Dr. {doctor.name} {doctor.lastname} deleted.')
                print('\n    ********************')
                break
            elif confirm == 'n':
                print('\n    ********************')

                print('\n    Deletion canceled.')
                print('\n    ********************')
                break
            else:
                print('\n    ********************')
                print('\n    Invalid input. Please enter "y" for yes or "n" for no.')
                print('\n    ********************')





def get_a_doctor_patients(doctor):
    # doctor = Doctor.get_by_name(doctor.name, doctor.lastname)
    if doctor:
        patients = doctor.list_a_doctor_patients()
        if patients:
            print('\n      ********************')
            print(f'\n      List of patients for Dr. {doctor.name} {doctor.lastname}')
            for i, patient in enumerate(patients, start=1):
                print(f'\n    {i}- {patient.name} {patient.lastname}')
            print('\n      ********************')  
            return patients 
        
        else:
            print('\n    ********************')
            print(f'\n    No patients found for Dr. {doctor.name} {doctor.lastname}.')
            print('\n    ********************')

            
    else:
        print('\n    ********************')
        print(f'\n    Doctor not found.')
        print('\n    ********************')
    

      
         


 # PYTHONPATH=. python -m utils.cli    



