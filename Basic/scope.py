# local scope
def myfunc1():
    x = 300
    print(x)
myfunc1()

def myfunc2():
    y = 300
    def myInnerFunc():
        print(y)
    myInnerFunc()
myfunc2()

# global scope
a = 300
def myfunc3():
    print(a)
myfunc3()
print(a)

b = 300
def myfunc4():
    b = 200
    print(b)
myfunc4()
print(b)

# global keyword
def myfunc5():
    global c
    c = 300
myfunc5()
print(c)

d = 300
def myfunc6():
    global d
    d = 200
myfunc6()
print(d)