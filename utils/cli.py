
# cli.py
from utils.helpers import *
from seed import seed_database
import sys
# Goodbye
def patient_enumerate_list():

    patients = Patient.get_all()
    print('\n    list of patients:\n')
    for i, patient in enumerate(patients, start = 1):
        print(f'{i}- {patient.name} {patient.lastname}\n')
    try:
        choice = int(input('\n    Select a patient by number: \n'))
        selected_patient = patients[choice - 1]
        print(f'    \n{selected_patient.name} {selected_patient.lastname} age: {selected_patient.age} disease: {selected_patient.disease}\n')
    except (IndexError, ValueError):
        print('\n    Invalid choice. Please enter a number corresponding to a patient.')

def patients_info():
   while True:
       print("    \nPatients Menu:\n")
       print('Press " m " to go back to the main menu.\n')
     
       print("pl) Patients List:\n")
       print("pu) Update a patient's information\n")
       print("pa) Add a new patient\n")
       print("pd) Delete a patient\n")
    #    print('m) Main Menu\n')
       print("0- Exit\n")

       choice = input('\n    Enter your choice: \n').lower()
       if choice == 'pl':
            patient_enumerate_list()
       elif choice == 'pu':
            update_patient()
       elif choice == 'pa':
            add_patient()
       elif choice == 'pd':
            delete_patient()
       elif choice == 'm':
           main_menu()
       elif choice == '0':
            sys.exit('    Goodbye!')
       else:
            print('    Invalid choice. Please try again.\n')

def doctors_enumerate_list():
    
    doctors = Doctor.get_all()
    print(('\n    list of doctors:\n'))
    for i, doctor in enumerate(doctors, start = 1):
        print(f'{i}- {doctor.name} {doctor.lastname}')
    try:
        choice = int(input('Select a doctor by number: \n'))
        selected_doctor = doctors[choice - 1]
        print(f'{selected_doctor.name} {selected_doctor.lastname} Speciality: {selected_doctor.specialty}')
    except IndexError:
        print('Invalid number, plaese try again.')

        




def doctors_info():
    while True:
        print('\n    Doctors Menu:\n')
        print('Press " m " to go back to the main menu.\n')
        print('dl) Doctors List:\n')
        print('dp) List of patient for a doctor:\n')
        print("du) Update a doctor's information\n")
        print("da) Add a new doctor\n")
        print("dd) Delete a doctor\n")
        # print('m) Main Menu\n')
        print("0- Exit\n")

        choice = input('\n    Enter your choice: \n').lower()
        if choice == 'dl':
            doctors_list()
        elif choice == 'dp':
            get_a_doctor_patients()
        elif choice == 'du':
            update_doctor()
        elif choice == 'da':
            add_doctor()
        elif choice == 'dd':
            delete_doctor()
        elif choice == 'm':
            main_menu()
        elif choice == '0':
            sys.exit('    Goodbye!\n')
        else:
            print('    Invalid choice. Please try again.\n')





def main_menu():
    while True:
        print('\n    *****  Main Menu  *****\n')
        print('    Select a number:\n')
        print('1- Doctors Info...\n')
        print('2- Patients Info...\n')
        print('0- Exit...\n')
        choice = input('\n    Enter your  choice: \n')
        if choice == '1':
            doctors_info()
        elif choice == '2':
            patients_info()
        elif choice == '0':
            sys.exit('    Goodbye!\n')
        else:
            print('    Invalid number. Please try again.\n')


if __name__ == "__main__":
    main_menu()

# PYTHONPATH=. python -m utils.cli