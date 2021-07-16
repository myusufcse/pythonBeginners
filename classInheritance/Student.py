class Student:
    name = "null"
    roll_no = "0"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def printDetails(self):
        print("Student Roll Number is", self.roll_no)
        print("Student Name is", str(self.name).capitalize())


s1 = Student("yu", 1)
s1.printDetails()
s2 = Student("ay", 2)
s2.printDetails()
