import json

# json converts to python
a = '{ "Name" : "Camus", "Age" : 25, "City" : "Sukabumi"}'
b = json.loads(a)
print(b["City"])

# python object converts to json
x = {
    "Name" : "Huawei",
    "Series" : "P30 Pro",
    "Price" : "Rp 9'000'000.00-"
}
y = json.dumps(x)
print(y)


# you can convert python objects of the following types, into json strings
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# example for all legal data types
identity = {
    "name" : "John",
    "age" : 30,
    "married" : True,
    "divorced" : False,
    "children" : ("Ann","Billy"),
    "pets" : None,
    "cars" : [
        {"model" : "BMW 230", "mpg": 27.5},
        {"model" : "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(identity))
# separators=(". ", " = ") is optional
print(json.dumps(identity, indent=2, separators=(". ", " = ")))
# , sort_keys=True for sorting the result alphabetically