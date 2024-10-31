

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


        