# doctor.py 

import sqlite3
CONN = sqlite3.connect('patient_tracking.db')
CURSOR = CONN.cursor()
class Doctor:
    all = {}
    def __init__(self, name, lastname, specialty, id=None):
        self.id = id 
        self.name = name
        self.lastname = lastname
        self.specialty = specialty
        if self.id:
            Doctor.all[self.id] = self
        
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 2:
            self._name = name
        else:
            raise ValueError('Name must be a string longer than 2 characters.')


    
    @property
    def lastname(self):
        return self._lastname
    @lastname.setter
    def lastname(self, lastname):
        if isinstance(lastname, str) and len(lastname) > 2:
            self._lastname = lastname
        else:
            raise ValueError('Lastname must be a string longer than 2 characters.')

    
    @property
    def specialty(self):
        return self._specialty
    @specialty.setter
    def specialty(self, specialty):
        if isinstance(specialty, str) and len(specialty) > 2:
            self._specialty = specialty
        else:
            raise ValueError('Specialty must be a string longer than 2 characters.')
    

    @classmethod
    def drop_table(cls):
        sql = '''
           DROP TABLE IF EXISTS doctors
         '''
        CURSOR.execute(sql)
        CONN.commit()

   
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            lastname TEXT NOT NULL,
            specialty TEXT NOT NULL
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        
        '''Insert the Doctor instance into db and save the id.'''
        sql = '''
             INSERT INTO doctors(name, lastname, specialty)
             VALUES(?,?,?)

         '''
        CURSOR.execute(sql, (self.name, self.lastname, self.specialty))
        CONN.commit()
        self.id = CURSOR.lastrowid
        Doctor.all[self.id] = self

    @classmethod
    def create(cls, name, lastname, specialty):
        '''Creates an instance of the class and saves in db.'''
        doctor = cls(name, lastname, specialty)
        doctor.save()
        return doctor if doctor else None

    @classmethod
    def instance_from_db(cls, row):
        '''Return a doctor instance based on a database row.'''
        if row is None:
            return None

        doctor_id = row[0]
        doctor = cls.all.get(doctor_id)
        if doctor:
            doctor.name = row[1]
            doctor.lastname = row[2]
            doctor.specialty = row[3]
        else:
            doctor = cls(row[1], row[2], row[3])
            doctor.id = row[0]
            cls.all[doctor.id] = doctor
        return doctor
    
    @classmethod
    def find_by_id(cls, id):
        '''Find and return a doctor instance by ID from the doctors table.'''
    
        sql = '''
             SELECT *
             FROM doctors
             WHERE id = ?
          ''' 
        row = CURSOR.execute(sql, (id,)).fetchone()
        doctor = cls.instance_from_db(row)
        return doctor if doctor else None
    
    @classmethod
    def get_all(cls):
        sql = '''
           SELECT  *
           FROM doctors
           
         '''
        doctors = []
        rows = CURSOR.execute(sql).fetchall()
        for row in rows:
            doctor = cls.instance_from_db(row)
            doctors.append(doctor)
        return doctors if doctors else None

    def update(self, name, lastname, specialty):
        self.name = name
        self.lastname = lastname
        self.specialty = specialty
        
        sql = '''
             UPDATE doctors
             SET name = ?, lastname = ?, specialty = ?
             WHERE id = ?
         '''
        CURSOR.execute(sql, (self.name, self.lastname, self.specialty, self.id))
        CONN.commit()

    

    def delete(self, doctor_id):
        sql = ''' 
            DELETE FROM doctors
            WHERE id = ?
        ''' 
        CURSOR.execute(sql, (doctor_id,))
        CONN.commit()

        if doctor_id in self.__class__.all:
            del self.__class__.all[doctor_id]  
            print(f"Doctor with ID {doctor_id} has been deleted.")
        else:
            print(f"No doctor found with ID {doctor_id}.")

    # def list_a_doctor_patients(self, doctor_id):
    #     from patient import Patient
    #     patients_list = []
    #     sql = '''
    #         SELECT * FROM patients
    #         WHERE doctor_id = ?
    #      '''
    #     CURSOR.execute(sql, (doctor_id,))
    #     CONN.commit()
    #     rows = Patient.instance_from_db(doctor_id).fetchall()
    #     for row in rows:
    #         patients_list.append(row)
    #     return patients_list if patients_list else None
        
    def list_a_doctor_patients(self, doctor_id):
        from models.patient import Patient
        patients_list = []
        sql = '''
        SELECT * FROM patients
        WHERE doctor_id = ?
         '''
        CURSOR.execute(sql, (doctor_id,))
        rows = CURSOR.fetchall()  # Fetch all matching rows
        if not rows:
            print('No patient found for this doctor.')
            return None


        # Transform rows into Patient instances
        for row in rows:
            
            patient = Patient.instance_from_db(row)  # Create Patient instance from each row
            if patient:
                patients_list.append(patient)
            # else:
            #     print('No patient found for this doctor.')
                    
        return patients_list if patients_list else None

     

    
         # PYTHONPATH=. python -m utils.cli

      

