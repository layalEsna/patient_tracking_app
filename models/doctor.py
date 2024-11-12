# doctor.py 

# import sqlite3
# CONN = sqlite3.connect('patient_tracking.db')
# CURSOR = CONN.cursor()
# from utils.db import Database

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

    # models/doctor.py


    


    
    # @classmethod
    # def create(cls, name, lastname, specialty):
    #     existing_doctor = cls.find_by_id(id)
    #     if existing_doctor:
    #         return existing_doctor

    #     sql = '''
    #     INSERT INTO doctors (name, lastname, specialty)
    #     VALUES (?, ?, ?)
    #     '''
    #     cursor = CONN.cursor()
    #     cursor.execute(sql, (name, lastname, specialty))
    #     doctor_id = cursor.lastrowid
    #     CONN.commit()
    #     cursor.close()

    #     return cls.find_by_id(doctor_id)
    
    @classmethod
    def get_by_name(cls, name, lastname):
        sql = '''
        SELECT * FROM doctors
        WHERE name = ? AND lastname = ?
        '''
        cursor = CONN.cursor()
        cursor.execute(sql, (name, lastname))
        result = cursor.fetchone()
        cursor.close()

        if result:
            # Unpack result assuming it includes `id`, `name`, `lastname`, `specialty`
            id, name, lastname, specialty = result
            return cls(name, lastname, specialty, id=id)
        return None


    

    

    # @classmethod
    # def create(cls, name, lastname, specialty):
    #     '''Creates an instance of the class and saves in db.'''
    #     existing_doctor = cls.find_by_id()
    #     if existing_doctor:
    #         return existing_doctor
    #     doctor = cls(name, lastname, specialty)
    #     doctor.save()
    #     return doctor if doctor else None

    @classmethod
    def create(cls, name, lastname, specialty):
        existing_doctor = cls.get_by_name(name, lastname)
        if existing_doctor:
            return existing_doctor
        else:
   
            new_doctor = cls(name, lastname, specialty)
            new_doctor.save()
            return new_doctor 


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
       
        rows = CURSOR.execute(sql).fetchall()
        return[cls.instance_from_db(row) for row in rows]

    # def update(self, name,lastname, specialty):
        
    #     self.name = name
    #     self.lastname = lastname
    #     self.specialty = specialty
        
    #     sql = '''
    #          UPDATE doctors
    #          SET name = ?, lastname = ?, specialty = ?
    #          WHERE id = ?
    #      '''
    #     CURSOR.execute(sql, (self.name, self.lastname, self.specialty, self.id))
    #     CONN.commit()

    def update(self, name=None, lastname=None, specialty=None):
        '''Update the doctor's details and save to the database.'''
    
        # Update attributes only if a new value is provided
        if name:
            self.name = name
        if lastname:
            self.lastname = lastname
        if specialty:
            self.specialty = specialty

        sql = '''
         UPDATE doctors
         SET name = ?, lastname = ?, specialty = ?
         WHERE id = ?
         '''
        # Execute the update command with the updated details
        CURSOR.execute(sql, (self.name, self.lastname, self.specialty, self.id))
        CONN.commit()  # Make sure to commit changes to save them permanently


    
    @classmethod
    def delete(cls, doctor_id):
        sql = ''' 
            DELETE FROM doctors
            WHERE id = ?
        ''' 
        CURSOR.execute(sql, (doctor_id,))
        CONN.commit()

        if doctor_id in cls.all:
            del cls.all[doctor_id]  
            print(f"\n    Doctor with ID {doctor_id} has been deleted.\n")
        else:
            print(f"\n    No doctor found with ID {doctor_id}.")

    def list_a_doctor_patients(self):
        from models.patient import Patient

        sql = '''
           SELECT * FROM patients
           WHERE doctor_id = ?
         '''
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        if not rows:
            print('No patient found for this doctor.')
            return None

        return [Patient.instance_from_db(row) for row in rows]
    

    
     

    
    #     #  PYTHONPATH=. python -m utils.cli

      

