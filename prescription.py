class Prescription:
    def __init__(self,id,title,date,data):
        self.title= title
        self.id=id
        self.date= date
        self.data =data

    def getTitle(self):
        return self.title
    def getDate(self):
        return self.date
    def getData(self):
        return self.data

