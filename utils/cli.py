
# cli.py 

from utils.helpers import *
from seed import seed_database
from models.patient import Patient
from models.doctor import Doctor
import sys

def patient_enumerate_list():
    
        patients = Patient.get_all()
        print('\n    ********************')
        print('\n    List of Patients: ')
        for i, patient in enumerate(patients, start=1):
            print(f'\n    {i}- {patient.name} {patient.lastname}')

        print('\n    ********************')
        
        print('\n    Select a patient number to update or delete')
        print('\n    Enter "m" for Main Menu')
        print('\n    Enter 0 to exit the program')
        choice = input('\n    Select a patient by number, or enter an option: ').lower()

        if choice == 'm':
            main_menu()
            
        elif choice == '0':
            sys.exit('\n    Goodbye ✋!\n')

        try:
            choice = int(choice)
            selected_patient = patients[choice - 1]
            print('\n    ********************')
            print(f'\n    Selected: {selected_patient.name} {selected_patient.lastname}, Age: {selected_patient.age}, Disease: {selected_patient.disease}')
            
            doctor = Doctor.find_by_id(selected_patient.doctor_id)
            if doctor:
                print(f'\n    Physician: {doctor.name} {doctor.lastname}')
            else:
                print('\n    Physician information not found.')
                print('\n      ********************')
           
            while True:
                action = input(f'\n    Enter "u" to update {selected_patient.name} {selected_patient.lastname} or "d" to delete the patient: ').lower()
                
                if action == 'u':
                    update_patient(selected_patient.id)
                    break
                elif action == 'd':
                    delete_patient(selected_patient)
                    break

                else:
                    print('\n    Invalid action. Please enter "u" to update or "d" to delete a patient.')

        except IndexError:
            print('\n    Invalid choice. Please enter a number corresponding to a patient.')
        except ValueError:
            print('\n    Please enter a valid number, "m" for main menu, or "0" to exit.')




 

def patients_info():
    while True:
        print('\n    >>>>>> Patients Menu...')
        print('    Press " m " to go back to the main menu.\n')

        print("\n    pl) Patients List:\n")
        
        
        print("\n    ap) Add a new patient\n")
      
        
        
        print("\n    0- Exit\n")

        choice = input('\n    Enter your choice: ').lower()
        if choice == 'pl':
            patient_enumerate_list()  
         
        elif choice == 'ap':
            add_patient()
        
        elif choice == 'm':
            main_menu()
        elif choice == '0':
            sys.exit('\n    Goodbye ✋!\n')
        else:
            print('\n    Invalid choice. Please try again.')





def doctor_enumerate_list():
  

    doctors = Doctor.get_all()
    print('\n    ********************')
    print('\n    List of Doctors:')
    for i, doctor in enumerate(doctors, start=1):
      print(f'\n    {i}- {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty}')
    print('\n   ********************')

    

    print('\n    Select a doctor number to update, delete, or view their patients')
    print('\n    Enter "m" for Main Menu')
    print('\n    Enter 0 to exit the program')

    choice = input('\n   Select a doctor by number or enter an option: ').lower()

    if choice == 'm':
      main_menu()
    
    elif choice == '0':
      sys.exit('\n    Goodbye ✋!\n')
    else:
      try:
        choice = int(choice)
        if choice < 1 or choice > len(doctors):
            print(f'\n    Invalid number. Please select a number between 1 and {len(doctors)}.')
        else:
            selected_doctor = doctors[choice - 1]  
            print('\n    ********************')
            print(f'\n    Selected: {selected_doctor.name} {selected_doctor.lastname}')
            print(f'\n    Specialty: {selected_doctor.specialty}')
            print('      ********************\n')
            print('\n    Enter "m" to go back to main menu or "0" to exit the program.')
        
            action = input(f'\n    Enter "u" to update {selected_doctor.name} {selected_doctor.lastname}, "d" to delete the doctor, or "p" to view their patients: ').lower()
            # print('\n    Enter "m" to go back to main menu or "0" to exit the program.')
        

            if action == 'u':
                update_doctor(selected_doctor)
            elif action == '0':
                sys.exit("\n    Good bye 🤚!\n")
            elif action == 'm':
                main_menu()

            elif action == 'd':
                delete_doctor(selected_doctor)

            elif action == 'p':
                get_a_doctor_patients(selected_doctor)

            else:
                 print('\n    Invalid action. Please enter "u" to update, "d" to delete, or "dp" to view patients.')
      except ValueError:  
            print('\n    Invalid input. Please enter a valid number, "m" for main menu, or "0" to exit.')


def doctors_info():
    while True:
        print('\n    >>>>>> Doctors Menu...')
        print('\n    Press " m " to go back to the main menu.')
        print('\n    dl) Doctors List:')
        print("\n    ad) Add a new doctor")
        print("\n    0- Exit")

        choice = input('\n    Enter your choice: ').lower()
        if choice == 'dl':
           doctor_enumerate_list()

        
        elif choice == 'ad':
            add_doctor()
        
        elif choice == 'm':
            main_menu()
        elif choice == '0':
            sys.exit('\n    Goodbye ✋!\n')
        else:
            print('\n    Invalid choice. Please try again.')



def main_menu():
    while True:
        print('\n   * ** *** **** *****  Main Menu  ***** **** *** ** *\n')
        print('\n                    Select a number: ')
        print('\n                    1- Doctors Info...')
        print('\n                    2- Patients Info...')
        print('\n                    0- Exit...')
        choice = input('\n    Enter your  choice: ')
        if choice == '1':
            doctors_info()
        elif choice == '2':
            patients_info()
        elif choice == '0':
            sys.exit('\n    Goodbye 🤚!\n')
        else:
            print('\n    Invalid entry. Please try again.')


if __name__ == "__main__":
    seed_database()
    main_menu()

# PYTHONPATH=. python -m utils.cli   bbbbbb