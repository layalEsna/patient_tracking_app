        



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
