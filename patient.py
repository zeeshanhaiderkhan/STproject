class Patient:
    def __init__(self,id,name,cnic,phone,dob,doc=None,prescriptions=[],reports=[],dietPlans=[]):
        self.name = name
        self.id = id
        self.cnic = cnic
        self.phone = phone
        self.dob = dob
        self.doc = doc
        self.prescriptions = prescriptions
        self.reports = reports
        self.dietPlans = dietPlans

    def getDoctor(self):
        return self.doc

    def getReports(self):
        return self.reports
    def getPrescriptions(self):
        return self.prescriptions
    def getDietPlans(self):
        return self.dietPlans

    def getLatestReport(self):
        return self.reports[-1]

    def getLatestPrescription(self):
        return self.prescriptions[-1]
    
    def getLatestDietPlan(self):
        return self.dietPlans[-1]

    def getAge(self):
        return 2021-self.dob
    def addReport(self,report):
        try:
            self.reports.append(report)
            return True
        except:
            self.reports=[]
            return False
    def addDietPlan(self,dietPlan):
        try:
            self.dietPlans.append(dietPlan)
            return True
        except:
            self.dietPlans=[]
            return False

    def addPrescription(self,prescription):
        try:
            self.prescriptions.append(prescription)
            return True
        except:
            self.prescriptions = []
            return False
    def getTotalReports(self):
        return len(self.reports)
    def getTotalPrescriptions(self):
        return len(self.prescriptions)
    def getTotalDietPlans(self):
        return len(self.dietPlans)
    

