# create class
class myClass:
    x = 5
print(myClass)

# create object
p1 = myClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Haris", 25)
print(p1.name)
print(p1.age)

class Actor:
    def __init__(self, name, age, race):
        self.name = name
        self.age = age
        self.race = race
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Actor("Camus", 25, "Sunda")
p1.myfunc()