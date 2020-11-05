# create parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
# use the Person class to create the object and executed by printname method
x = Person("Haris", "Hidayat")
x.printname()

# create a child
class Student(Person):
   pass
    # other solution is creating __init__ instead of pass keyword
    # def __init__(self, fname, lname):
    #   Person.__init__(self, fname, lname)
    # super() function will make the child class inherite all the methods and properties from its parent
    # super().__init__(fname, lname)
    # child class can also add new property
    # example self.graduationyear = 2020
    # or self.graduationyear = year
x = Student("Camus", "Harmonia")
x.printname()

class Uni_Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Uni_Student("Haris", "Hidayat", 2020)
x.welcome()