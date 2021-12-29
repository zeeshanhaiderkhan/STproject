class Doctor:
    def __init__(self,id,name,cnic,phone,dob,sex,patients=[]):
        self.name  = name
        self.id = id
        self.cnic = cnic
        self.phone = phone
        self.dob = dob
        self.sex = sex
        self.patients = patients

    def getAge(self):
        return 2021 - dob

    def getLatestPatient(self):
        try:
            return self.patients[-1]
        except:
            return False
    def getTotalPatients(self):
        return len(self.patients)


