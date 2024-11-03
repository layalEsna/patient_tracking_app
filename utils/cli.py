
# cli.py
from utils.helpers import *
from seed import seed_database
import sys

def display_welcome_and_instructions():
    print("Welcome to the Patient Tracking App\n")
    print("Please select an option:\n")
    print("1. Display doctors list\n")
    print("2. Update a doctor's information\n")
    print("3. Add a new doctor\n")
    print("4. Display patients list\n")
    print("5. Update a patient's information\n")
    print("6. Add a new patient\n")
    print("7. Delete a doctor\n")
    print("8. Delete a patient\n")
    print("9. Exit\n")

def exit_program():
    print('Goodbye!')
    sys.exit()

def main():
    seed_database()  
    while True:
        display_welcome_and_instructions()
        choice = input("Enter your choice: ")

        if choice == '1':
            doctors_list()
        elif choice == '2':
            update_doctor()
        elif choice == '3':
            add_doctor()
        elif choice == '4':
            patients_list()
        elif choice == '5':
            update_patient()
        elif choice == '6':
            add_patient()
        elif choice == '7':
            delete_doctor()
        elif choice == '8':
            delete_patient()
        elif choice == '9':
            exit_program()
        else:
            print('Invalid choice, please try again.')

if __name__ == '__main__':
    main()
# PYTHONPATH=. python -m utils.cli
