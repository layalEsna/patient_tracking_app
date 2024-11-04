
# cli.py
from utils.helpers import *
from seed import seed_database
import sys

def doctors_info():
    while True:
        print('\nDoctors Information:\n')
        print('a) Doctors List:\n')
        print("b) Update a doctor's information\n")
        print("c) Add a new doctor\n")
        print("d) Delete a doctor\n")
        print('m) Main Menu\n')
        print("0- Exit\n")

        choice = input('\nEnter your choice: \n').lower()
        if choice == 'a':
            doctors_list()
        elif choice == 'b':
            update_doctor()
        elif choice == 'c':
            add_doctor()
        elif choice == 'd':
            delete_doctor()
        elif choice == 'm':
            main_menu()
        elif choice == '0':
            sys.exit('Goodbye!\n')
        else:
            print('Invalid choice. Please try again.\n')



def patients_info():
   while True:
       print("\nPatients information:\n")
       print("e) Patients List:\n")
       print("f) Update a patient's information\n")
       print("g) Add a new patient\n")
       print("h) Delete a patient\n")
       print('m) Main Menu\n')
       print("0- Exit\n")

       choice = input('Enter your choice: \n').lower()
       if choice == 'e':
            patients_list()
       elif choice == 'f':
            update_patient()
       elif choice == 'g':
            add_patient()
       elif choice == 'h':
            delete_patient()
       elif choice == 'm':
           main_menu()
       elif choice == '0':
            sys.exit('Goodbye!')
       else:
            print('Invalis choice. Please try again.\n')


def main_menu():
    while True:
        print('\n*****Main Menu*****\n')
        print('Select a number:\n')
        print('1- Doctors Info...\n')
        print('2-Patients Info...\n')
        print('0- Exit...\n')
        choice = input('\nEnter your  choice: \n')
        if choice == '1':
            doctors_info()
        elif choice == '2':
            patients_info()
        elif choice == '0':
            sys.exit('Goodbye\n')
        else:
            print('Invalid number. Please try again.\n')


if __name__ == "__main__":
    main_menu()
    
# PYTHONPATH=. python -m utils.cli