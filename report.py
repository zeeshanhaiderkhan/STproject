class Report:
    def __init__(self,id,title,date,data):
        self.title= title
        self.id=id
        self.date = date
        self.data =data

    def getData(self):
        return self.data
    def getDate(self):
        return self.date
    def getTitle(self):
        return self.title
