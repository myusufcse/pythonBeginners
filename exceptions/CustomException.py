class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def printException(self):
        print("My Custom Exception msg :", self.msg)


try:
    raise Accident("I Raised Custom Exception Now")
except Accident as a:
    a.printException()