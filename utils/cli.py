
# cli.py
from utils.helpers import *
import sys

def exit_program():
    print('Goodbye!')
    sys.exit()
    
def main():
    while True:
        display_welcome_and_instructions()
        choice = input()

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


