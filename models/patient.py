

class Patient:
    all = []
    def __init__(self, name, lastname, age, disease, doctor_id, id=None):
        self.id = id or len(Patient.all) +1
        self.name = name
        self.lastname = lastname
        self.age = age
        self.disease = disease
        self.doctor_id = doctor_id
        Patient.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 2:
            self._name = name

    
    @property
    def lastname(self):
        return self._lastname
    @lastname.setter
    def lastname(self, lastname):
        if isinstance(lastname, str) and len(lastname) > 2:
            self._lastname = lastname
            

    
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if isinstance(age, int) and 18 >= age >= 100:
            self._age = age


