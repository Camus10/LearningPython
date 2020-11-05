def my_function():
    print("This is function")
my_function()

def new_function(fname):
    print(fname + " Refsnes")
new_function("Haris")
new_function("Camus")

# if number of aguments is unknown
def his_function(*kids):
    print("The youngest child is " + kids[2])
his_function("Emil", "Tobias", "Linus")

def child_function(child3, child2, child1):
    print("The youngest child is " + child3)
child_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# if number of keyword arguments is unknown
def kid_function(**kid):
  print("His last name is " + kid["lname"])
kid_function(fname = "Tobias", lname = "Refsnes")

def country_function(country = "Norway"):
  print("I am from " + country)
country_function("Sweden")
country_function("India")
country_function()
country_function("Brazil")

def food_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
food_function(fruits)

def multiple_function(x):
    return 5 * x
print(multiple_function(3))
print(multiple_function(5))
print(multiple_function(9))