
# cli.py 

from utils.helpers import *
from seed import seed_database
from models.patient import Patient
from models.doctor import Doctor
import sys


def patient_enumerate_list():
    
        patients = Patient.get_all()
        print('\n    ********************\n')
        print('\n    List of Patients:\n')
        for i, patient in enumerate(patients, start=1):
            print(f'\n    {i}- {patient.name} {patient.lastname}\n')

        print('\n    ********************\n')
        
        print('\n    Select a patient number to update or delete\n')
        print('\n    Enter "m" for Main Menu\n')
        print('\n    Enter 0 to exit the program\n')
        choice = input('\n    Select a patient by number, or enter an option: \n').lower()

        if choice == 'm':
            main_menu()
            
        elif choice == '0':
            sys.exit('    Goodbye!')

        try:
            choice = int(choice)
            selected_patient = patients[choice - 1]
            print('\n    ********************')
            print(f'\n    Selected: {selected_patient.name} {selected_patient.lastname}, Age: {selected_patient.age}, Disease: {selected_patient.disease}\n')
            
            doctor = Doctor.find_by_id(selected_patient.doctor_id)
            if doctor:
                print(f'\n    Physician: {doctor.name} {doctor.lastname}\n')
            else:
                print('\n    Physician information not found.\n')
                print('      ********************\n')
           
            while True:
                action = input(f'\n    Enter "u" to update {selected_patient.name} {selected_patient.lastname} or "d" to delete the patient: ').lower()
                
                if action == 'u':
                    update_patient(selected_patient.id)
                    break
                elif action == 'd':
                    delete_patient(selected_patient)
                    break

                else:
                    print('\n    Invalid action. Please enter "u" to update or "d" to delete a patient.\n')

        except IndexError:
            print('\n    Invalid choice. Please enter a number corresponding to a patient.\n')
        except ValueError:
            print('\n    Please enter a valid number, "m" for main menu, or "0" to exit.\n')




 

def patients_info():
    while True:
        print("\n    *** Patients Menu...\n")
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
            sys.exit('\n    Goodbye!')
        else:
            print('\n    Invalid choice. Please try again.\n')





def doctor_enumerate_list():
  

    doctors = Doctor.get_all()
    print('\n ********************\n')
    print('\n List of Doctors:\n')
    for i, doctor in enumerate(doctors, start=1):
      print(f'\n {i}- {doctor.name} {doctor.lastname}, Specialty: {doctor.specialty}\n')
    print('\n ********************\n')

    

    print('\n Select a doctor number to update, delete, or view their patients\n')
    print('\n Enter "m" for Main Menu\n')
    print('\n Enter 0 to exit the program\n')

    choice = input('\n Select a doctor by number or enter an option: ').lower()

    if choice == 'm':
      main_menu()
    #   break
    elif choice == '0':
      sys.exit('\n Goodbye!\n')
    else:
      try:
        choice = int(choice)
        selected_doctor = doctors[choice - 1]  
        print('\n    ********************')
        print(f'\n Selected: {selected_doctor.name} {selected_doctor.lastname}\n')
        print(f'\n Specialty: {selected_doctor.specialty}\n')
        print('      ********************\n')
        action = input(f'\n Enter "u" to update {selected_doctor.name} {selected_doctor.lastname}, "d" to delete the doctor, or "p" to view their patients: ').lower()
        

        if action == 'u':
          update_doctor(selected_doctor)
        elif action == '0':
            sys.exit()
        elif action == 'm':
            main_menu()

        elif action == 'd':
          delete_doctor(selected_doctor)

        elif action == 'p':
          get_a_doctor_patients(selected_doctor)

        else:
          print('\n Invalid action. Please enter "u" to update, "d" to delete, or "dp" to view patients.\n')
      except ValueError:  
        print('\n Invalid input. Please enter a valid number, "m" for main menu, or "0" to exit.\n')


def doctors_info():
    while True:
        print('\n    *** Doctors Menu...\n')
        print('Press " m " to go back to the main menu.\n')
        print('dl) Doctors List:\n')
        print("ad) Add a new doctor\n")
        print("0- Exit\n")

        choice = input('\n    Enter your choice: ').lower()
        if choice == 'dl':
           doctor_enumerate_list()

        
        elif choice == 'ad':
            add_doctor()
        
        elif choice == 'm':
            main_menu()
        elif choice == '0':
            sys.exit('    Goodbye!\n')
        else:
            print('    Invalid choice. Please try again.\n')



def main_menu():
    while True:
        print('\n   * ** *** **** *****  Main Menu  ***** **** *** ** *\n')
        print('        Select a number:\n')
        print('\n        1- Doctors Info...\n')
        print('        2- Patients Info...\n')
        print('        0- Exit...\n')
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
    seed_database()
    main_menu()

# PYTHONPATH=. python -m utils.cli     J.Jm Walter, Specialty: Cardiology