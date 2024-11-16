
# helpers.py   Enter doctor's first name



from models.patient import Patient
from models.doctor import Doctor


# ----
def add_patient():
    while True:
        try:

            patient_name = input("\n    Enter patient's name: ")
            if not isinstance(patient_name, str) or len(patient_name) < 2:
                raise ValueError('\n    Name must be a string and more than 2 characters.')
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            patient_lastname = input("\n    Enter patient's last name: ")
            if not isinstance(patient_lastname, str) or len(patient_lastname) < 2:
                raise ValueError('\n    Last name must be a string and more than 2 characters.')
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            patient_age = int(input("\n    Enter patient's age: "))
            if not (18 <= patient_age <= 100):
                raise ValueError('\n    Age must be a number between 18 and 100 inclusive.')
            break
        except ValueError:
            print('\n    Age must be a number between 18 and 100 inclusive....')
        
    while True:
        try:
            disease = input("\n    Enter patient's disease: ")
            if not isinstance(disease, str) or len(disease) < 2:
                raise ValueError('\n    Disease must be a string and more than 2 characters.')
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            doctor_name = input("\n    Enter doctor's name: ") 
            if not isinstance(doctor_name, str) or len(doctor_name) < 2:
                raise ValueError('\n    Name must be a string and more than 2 characters.')
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            doctor_lastname = input("\n    Enter doctor's last name: ") 
            if not isinstance(doctor_lastname, str) or len(doctor_lastname) < 2:
                raise ValueError('\n     Last name must be a string and more than 2 characters.')
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            specialty =  input("\n    Enter doctor's specialty: ") 
            if not isinstance(specialty, str) or len(specialty) < 2:
                raise ValueError('\n    Specialty must be a string and more than 2 characters.')
            break
        except ValueError as e:
            print(e)
    

    doctor = Doctor.get_by_name(doctor_name, doctor_lastname)
    if not doctor:
        doctor = Doctor.create(doctor_name, doctor_lastname, specialty)
        print(f'\n    Success: New Doctor: {doctor_name} {doctor_lastname}: Specialty: {specialty} added.')

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
    #patient.update() 
    # patient_name = input(f"\n    Update Patient's name ({patient.name}): ") or patient.name
    # patient_lastname = input(f"\n    Update Patient's last name ({patient.lastname}): ") or patient.lastname
    while True:
        try:
            patient_name = input(f"\n    Update Patient's name ({patient.name}): ") or patient.name
            if not isinstance(patient_name, str) or len(patient_name) < 2:
                raise ValueError("\n    Patient's name must be a string and more than 2 characters.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            patient_lastname = input(f"\n    Update Patient's lastname ({patient.lastname}): ") or patient.lastname
            if not isinstance(patient_lastname, str) or len(patient_lastname) < 2:
                raise ValueError("\n    Patient's lastname must be a string and more than 2 characters.")
            break
        except ValueError as e:
            print(e)
    
    while True:
        try:
            age_input = input(f"\n    Update Patient's age ({patient.age}): ")
            if age_input.strip() == '':
                patient_age = patient.age
                break
            else:
                patient_age = int(age_input)
                if not (18 <= patient_age <= 100):
                    raise ValueError("\n    Patient's age must be a number and between 18 and 100 inclusive.")
                break
        except ValueError as e:
            print(e)

   
    while True:
        try:
            patient_disease = input(f"\n    Update Patient's disease ({patient.disease}): ") or patient.disease
            if not isinstance(patient_disease, str) or len(patient_disease) < 2:
                raise ValueError("\n    Patient's disease must be a string and more than 2 characters.")
            break
        except ValueError as e:
            print(e)

    
    if patient.doctor_id:
        doctor = Doctor.find_by_id(patient.doctor_id)
        if doctor:
            print(f'\n    Success: Patient {patient.name} {patient.lastname}, age {patient.age} Health condition: {patient.disease} updated.')
            print(f"\n    Physician: Dr. {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty}")
        else:

            while True:
                try:
                    confirm_add = input(f'\n    Do you want to assign a doctor to {patient.name} {patient.lastname} (y/n): ').lower()
                    if confirm_add == 'y':

                        new_doctor = add_doctor()
                        if new_doctor:
                            patient.doctor_id = new_doctor.id 
                            doctor.save()  
                            print(f'\n    Success: Patient {patient.name} {patient.lastname}, age {patient.age} Health condition: {patient.disease} updated.')
                            print(f"\n    New Physician: Dr. {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty}")
                        else:
                            print("\n    Doctor assignment failed. Please try again.")
                        break
                    elif confirm_add == 'n':
                        print('\n    No doctor assigned.')
                        break
                    else:
                        print('\n    Invalid input. Please enter "y" or "n".')
               


                except ValueError:
                    print('\n    No doctor assigned.')


     

               

def add_doctor():
    
    print('\n    Add New doctor...')
    while True:
        try:
            doctor_first_name = input(f"\n    Update doctor's name: ") 
            if not isinstance(doctor_first_name, str) or len(doctor_first_name) < 2:
                raise ValueError("\n    Doctor's name must be a string and more than 2 characters.")
            break
        except ValueError as e:
            print(e) 

    while True:
        try:

            doctor_lastname = input(f"\n    Enter doctor's last name: ") 
            if not isinstance(doctor_lastname, str) or len(doctor_lastname) < 2:
                raise ValueError('\n    Last name must be a string and more than 2 characters.')
            break
        except ValueError as e:
            print(e)
    

    while True:
        try:

            doctor_specialty = input(f"\n    Enter doctor's pecialty: ") 
            if not isinstance(doctor_specialty, str) or len(doctor_specialty) < 2:
                raise ValueError('\n    Specialty must be a string and more than 2 characters.')
            break
        except ValueError as e:
            print(e)
    



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
# def update_doctor(doctor):
#     if isinstance(doctor, Doctor): 
#         while True:
#           try:
#             doctor_name = input(f"\n    Update doctor's name ({doctor.name}): ") or doctor.name
#             if not isinstance(doctor_name, str) or len(doctor_name) < 2:
#                 raise ValueError("\n    Doctor's name must be a string and more than 2 characters.")
#             doctor.name = doctor_name
#             break
#             # doctor.name = doctor_name
#           except ValueError as e:
#             print(e)
#             # break
    
#         while True:
#           try:
#             doctor_lastname = input(f"\n    Update doctor's last name ({doctor.lastname}): ") or doctor.lastname
#             if not isinstance(doctor_lastname, str) or len(doctor_lastname) < 2:
#                 raise ValueError("\n    Doctor's last name must be a string and more than 2 characters.")
#             doctor.lastnaeme = doctor_lastname
#             break
#           except ValueError as e:
#               print(e)
#             # doctor.lastnaeme = doctor_lastname
            
#         while True:
#           try:
#             doctor_specialty = input(f"\n    Update doctor's specialty ({doctor.specialty}): ") or doctor.specialty
#             if not isinstance(doctor_specialty, str) or len(doctor_specialty) < 2:
#                 raise ValueError("\n    Doctor's specialty must be a string and more than 2 characters.")
#             doctor.specialty = doctor_specialty
#             break
#           except ValueError as e:
#               print(e)
#             # doctor.specialty = doctor_specialty
#             # break

#         doctor.update()
#         print('\n    ********************')
#         print(f'\n    Success: Dr {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty} updated')
#         print('\n    ********************')
#     else:
#             print('\n    Invalid doctor instance.') 

def update_doctor(doctor):
    if isinstance(doctor, Doctor): 
        while True:
            try:
                doctor_name = input(f"\n    Update doctor's name ({doctor.name}): ") or doctor.name
                if not isinstance(doctor_name, str) or len(doctor_name) < 2:
                    raise ValueError("\n    Doctor's name must be a string and more than 2 characters.")
                doctor.name = doctor_name
                break
            except ValueError as e:
                print(e)
    
        while True:
            try:
                doctor_lastname = input(f"\n    Update doctor's last name ({doctor.lastname}): ") or doctor.lastname
                if not isinstance(doctor_lastname, str) or len(doctor_lastname) < 2:
                    raise ValueError("\n    Doctor's last name must be a string and more than 2 characters.")
                doctor.lastname = doctor_lastname
                break
            except ValueError as e:
                print(e)
            
        while True:
            try:
                doctor_specialty = input(f"\n    Update doctor's specialty ({doctor.specialty}): ") or doctor.specialty
                if not isinstance(doctor_specialty, str) or len(doctor_specialty) < 2:
                    raise ValueError("\n    Doctor's specialty must be a string and more than 2 characters.")
                doctor.specialty = doctor_specialty
                break
            except ValueError as e:
                print(e)

        # Call the update method on the doctor instance
        doctor.update()
        print('\n    ********************')
        print(f'\n    Success: Dr {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty} updated')
        print('\n    ********************')
    else:
        print('\n    Invalid doctor instance.')


     
    
            
            
            
            


            

                



def delete_doctor(doctor):
    if isinstance(doctor, Doctor):
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



