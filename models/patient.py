
import sqlite3

CONN = sqlite3.connect('patient_tracking.db') 
CURSOR = CONN.cursor()


class Patient:
    all = {}
    
    def __init__(self, name, lastname, age, disease, doctor_id, id=None):
        self.id = id 
        self.name = name
        self.lastname = lastname
        self.age = age
        self.disease = disease
        self.doctor_id = doctor_id
        Patient.all[self.id] = self

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
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        
        if isinstance(age, int) and 18 <= age <= 100:  
            self._age = age
        else:
            raise ValueError('Age must be an integer between 18 and 100.')

    @property
    def disease(self):
        return self._disease
    
    @disease.setter
    def disease(self, disease):
        if isinstance(disease, str) and len(disease) > 2:
            self._disease = disease
        else:
            raise ValueError('disease must be a non-empty string.')
    
    @property
    def doctor_id(self):
        return self._doctor_id
    
    @doctor_id.setter
    def doctor_id(self, doctor_id):
        if isinstance(doctor_id, int):
            self._doctor_id = doctor_id
        else:
            raise ValueError('Doctor ID must be a positive integer.')

    @classmethod
    def create_table(cls):
        sql = '''
             CREATE TABLE IF NOT EXISTS patients (
             id INTEGER PRIMARY KEY,
             name TEXT,
             lastname TEXT,
             age INTEGER,
             disease TEXT,
             doctor_id INTEGER,
             FOREIGN KEY (doctor_id) REFERENCES doctors(id)
             )
          '''
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = '''
           DROP TABLE IF EXISTS patients
         '''
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        '''Insert the Patient instance into db and save the id.'''
        sql = '''
             INSERT INTO patients(name, lastname, age, disease, doctor_id)
             VALUES(?,?,?,?,?)
             '''
        CURSOR.execute(sql, (self.name, self.lastname, self.age, self.disease, self.doctor_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def get_by_name(cls, name, lastname):
        sql = '''
          SELECT * FROM patients
          WHERE name = ? AND lastname = ?
         '''
        row = CURSOR.execute(sql, (name, lastname))
        return cls.instance_from_db(row)
        
    
    
    
    @classmethod
    def create(cls, name, lastname,age, disease, doctor_id=None):
    
        existing_patient = cls.get_by_name(name, lastname)
        if existing_patient:
            return existing_patient
    
  
        patient = cls(name=name, lastname=lastname,age=age, disease=disease, doctor_id=doctor_id)
    
    
        patient.save()
    
        
        return patient


    
    @classmethod
    def instance_from_db(cls, row):
        '''Return a patient instance based on a database row.'''
        if not row:
            return None
        patient = cls.all.get(row[0])
        if patient:
            patient.name = row[1]
            patient.lastname = row[2]
            patient.age = row[3]
            patient.disease = row[4]
            patient.doctor_id = row[5]
        else:
            patient = cls(row[1], row[2], row[3], row[4], row[5])
            patient.id = row[0]
            cls.all[patient.id] = patient
        return patient if patient else None

    @classmethod
    def find_by_id(cls, id):
        '''Find and return a patient instance by ID from the patients table.'''
        sql = '''
         SELECT *
         FROM patients 
         WHERE id = ?

       '''
        row = CURSOR.execute(sql, (id,)).fetchone()
        patient = cls.instance_from_db(row)
        return patient if patient else None

    @classmethod
    def get_all(cls):
        sql = '''
         SELECT *
         FROM patients
       '''
        
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

   
    def update(self):
        sql = '''
          UPDATE patients 
          SET name = ?, lastname = ?, age = ?, disease = ?, doctor_id = ?
          WHERE id = ?
   
        '''
        CURSOR.execute(sql, (self.name, self.lastname,self.age, self.disease, self.doctor_id, self.id,))
        CONN.commit()

    

    def delete(self):
        sql = '''
         DELETE FROM patients
         WHERE id = ?
         '''
        CURSOR.execute(sql, (self.id, ))
        CONN.commit()

        del type(self).all[self.id] 
        self.id = None

   

#             # PYTHONPATH=. python -m utils.cli
       


       