class Father:
    def skills(self):
        print("sleeping, programming")


class Mother:
    def skills(self):
        print("scolding, cooking")


class Son(Father, Mother):
    def skills(self):
        # in order to call Father and Mother skills we have to use class name
        Father.skills(self)
        Mother.skills(self)
        # By default it will call only son skills if the above line don't exist
        print("playing, eating")


s = Son()
s.skills()
