import sqlite3
CONN = sqlite3.connect('your_database_name.db')
CURSOR = CONN.cursor()
class Doctor:
    all = []
    def __init__(self, name, lastname, specialty, id=None):
        self.id = id or len(Doctor.all) +1
        self.name = name
        self.lastname = lastname
        self.specialty = specialty
        Doctor.all.append(self)
        
    
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
    def Create_table(cls):

        sql = '''
             CREATE TABLE IF NOT EXISTS 
             doctors(
             id INTEGER PRIMARY KEY,
             name TEXT,
             lastname TEXT,
             specialty TEXT
             )
          '''
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = '''
           DROP TABLE IF EXISTS doctors
         '''
        CURSOR.execute(sql)
        CONN.commit()



        