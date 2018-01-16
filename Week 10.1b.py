from Studentdetails import*

firstname=input("Enter the student name: ")
lastname=input("Enter the student surname: ")
ID=input("Enter the Student ID: ")
course=input("Enter the course the student is in: ")

i=Student(firstname,lastname,ID,course)
i.studentdetails()
changecourse=input("Enter the student new course: ")
i.setCourse(changecourse)
print(i.getCourse())
i.studentdetails()
