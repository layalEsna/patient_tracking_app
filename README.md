Patient Management CLI

A Python Command-Line Interface (CLI) application for managing patients and doctors. This application allows users to add, view, update, and delete patient and doctor records. Additionally, it provides an interface for viewing the relationships between patients and their doctors.

Features:
. List, add, update, and delete patients

. List, add, update, and delete doctors

. View the doctor associated with each patient

.View the list of patients assigned to a specific doctor

Project Structure:

. models/: Contains the Patient and Doctor classes, which define the data models.

. utils/: Contains helper functions to support database operations and utilities.

. cli.py: The main CLI interface that interacts with the user and provides various options for managing patients and doctors.

. seed.py: Seeds the database with initial data for doctors and patients.

Requirements:
Ensure you have Python installed. It’s recommended to use a virtual environment to manage dependencies.

Dependencies:
. SQLite for data storage

Setup Instructions
1- git clone and cd to the project:
 https://github.com/layalEsna/patient_tracking_app

 2- nstall Dependencies If using Pipenv:  pipenv install

 3- Run Database Seeding Seed the database by running: PYTHONPATH=. python -m seed

 This command creates the necessary tables and populates them with initial data.


Here’s a README file template based on your project setup. This template includes sections to explain the project, its setup, usage, and a breakdown of the functionality.

Patient Management CLI
A Python Command-Line Interface (CLI) application for managing patients and doctors. This application allows users to add, view, update, and delete patient and doctor records. Additionally, it provides an interface for viewing the relationships between patients and their doctors.

Features
List, add, update, and delete patients
List, add, update, and delete doctors
View the doctor associated with each patient
View the list of patients assigned to a specific doctor
Project Structure
The project is organized into several modules:

cli.py: The main CLI interface that interacts with the user and provides various options for managing patients and doctors.
seed.py: Seeds the database with initial data for doctors and patients.
models/: Contains the Patient and Doctor classes, which define the data models.
utils/: Contains helper functions to support database operations and utilities.
Requirements
Ensure you have Python installed. It’s recommended to use a virtual environment to manage dependencies.

Dependencies
SQLite for data storage
Any additional libraries specified in your requirements.txt or managed with Pipenv
Setup Instructions
Clone the Repository



git clone https://github.com/layalEsna/patient_tracking_app
cd <project-folder>
Install Dependencies If using Pipenv:

bash
Copy code
pipenv install
Run Database Seeding Seed the database by running:

bash
Copy code
PYTHONPATH=. python -m seed
This command creates the necessary tables and populates them with initial data.

Usage:
Start the CLI by running: PYTHONPATH=. python -m utils.cli  

Main Menu
1 - Doctors Info: Access options related to managing doctors, including listing, adding, updating, and deleting doctor records.
2 - Patients Info: Access options related to managing patients, including listing, adding, updating, and deleting patient records.
0 - Exit: Exit the application.

Doctors Menu Options
1- List Doctors: Shows all doctors in the system with their specialties.
2- Add New Doctor: Prompts to add a new doctor to the database.
3- Update or Delete: Select a doctor to update or delete their information or view their list of patients.

Patients Menu Options
1- List Patients: Displays a list of all patients with their assigned doctor information.
2- Add New Patient: Allows adding a new patient and assigns them to a doctor.
3- Update or Delete: Select a patient to update or delete their information.

Additional Commands
. Seed Database: Run seed_database(reset=True) in seed.py to reset and populate the database tables.
. Database Models: The Patient and Doctor classes contain methods for creating, updating, and deleting records.

Project Details
. Patient Class: Manages patients with properties such as name, age, disease, and associated doctor.
. Doctor Class: Manages doctors with properties like name, specialty, and associated patients.

License:
This project is licensed under the MIT License.









