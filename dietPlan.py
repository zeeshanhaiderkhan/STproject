class DietPlan:
    def __init__(self,id,title,date,data):
        self.id = id
        self.title= title
        self.date = date
        self.data= data

    def getTitle(self):
        return self.title
    def getDate(self):
        return self.date
    def getData(self):
        return self.data
    def __str__(self):
        return self.id + " "+ self.title
