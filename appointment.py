class TimeSlot:
    def __init__(self,starttime,endtime):
        if starttime[0]>23 and starttime[0]<0:
            raise Exception("Invalid Starttime")
        elif endtime[1]>59 and endtime[1]<0:
            raise Exception("Invalid Endtime")
        self.starttime = starttime #(10,21)
        self.endtime =endtime     #(10,21) == 10:21

    def getTotalTime(self):
        return (endtime[0]-starttime[0],endtime[1]-starttime[1])



class Appointment:
    def __init__(self,patient,doctor,timeslot,payment):
        self.patient = patient #type patient
        self.doctor = doctor #type doctor
        self.timeslot = timeslot #type:timeslot
        self.payment = payment #bool
    def getTimeSlot(self):
        return timeslot
    def getStartTime(self):
        return self.timeslot.starttime
    def getEndTime(self):
        return self.timeslot.endtime
    def getTotalTime(self):
        return self.timeslot.getTotalTime()
    def __str__(self):
        return self.patient.name+" "+self.timeslot.starttime
