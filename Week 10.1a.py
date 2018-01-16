class Student:
    def __init__(self,firstname,lastname,ID,course):
        self.firstname=firstname
        self.lastname=lastname
        self.ID=ID
        self.course=course

    def setFirstname(self,firstname):
        self.firstname=firstname
    def setLastname(self,lastname):
        self.lastname=lastname
    def setID(self,ID):
        self.ID=ID
    def setCourse(self,course):
        self.course=course

    def getFirstname(self):
        return self.firstname
    def getLastname(self):
        return self.lastname
    def getCourse(self):
        return self.course
    def getID(self):
        return self.ID

    def studentdetails(self):
        print(self.firstname,self.lastname,self.ID,self.course)

a = Student("Pankaj","Singh","21360293","Computer Science")
a.studentdetails()
