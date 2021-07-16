from Student import Student as s


class CSE_Group(s):
    def __init__(self):
        super().__init__("rock", 3)
        self.major = "Computer Science"

    def printDetails(self):
        super().printDetails()
        print(str(self.name).capitalize(), "Major subject is", self.major)


c = CSE_Group()
c.printDetails()
