# 🏥 Patient Management CLI

A **Python Command-Line Interface (CLI)** application for managing patients and doctors. This tool allows users to add, view, update, and delete patient and doctor records, plus explore the relationships between patients and their doctors.

---

## 🚀 Features

- Manage patients: list, add, update, and delete
- Manage doctors: list, add, update, and delete
- View the doctor associated with each patient
- View patients assigned to a specific doctor

---

## 📁 Project Structure

- `cli.py`: Main CLI interface to interact with users and manage records.
- `seed.py`: Script to seed the database with initial data.
- `models/`: Contains `Patient` and `Doctor` classes defining data models.
- `utils/`: Helper functions for database operations and utilities.

---

## 🛠 Requirements & Dependencies

- Python 3.8+ (virtual environment recommended)
- SQLite (for data storage)
- Additional dependencies handled via `requirements.txt` or Pipenv

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/layalEsna/patient_tracking_app.git
cd patient_tracking_app
2. Install dependencies
If using Pipenv:



pipenv install
Alternatively, use pip with requirements.txt if available:



pip install -r requirements.txt
3. Seed the database
Populate the database tables with initial data:



PYTHONPATH=. python -m seed
▶️ Usage
Start the CLI application:



PYTHONPATH=. python -m utils.cli
Main Menu Options
Option	Description
1	Doctors Info: Manage doctors (list, add, update, delete)
2	Patients Info: Manage patients (list, add, update, delete)
0	Exit the application

Doctors Menu
List Doctors: View all doctors with their specialties

Add New Doctor: Add a new doctor record

Update or Delete: Modify or remove doctor info; view assigned patients

Patients Menu
List Patients: View all patients with their assigned doctors

Add New Patient: Add a patient and assign to a doctor

Update or Delete: Modify or remove patient info

🔧 Additional Information
To reset and seed the database, run seed_database(reset=True) in seed.py.

The Patient and Doctor classes manage CRUD operations internally.

The CLI is designed for easy navigation and quick data management.

📜 License
This project is licensed under the MIT License.

💡 Author
Developed with ❤️ by Amene Esnaashari