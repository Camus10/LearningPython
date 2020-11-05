# file handling mode
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

a = open("demofile.txt")    # similar with f = open("demofile.txt", "rt")
# "r" for read, and "t" for text are the default values
print(a.read())

b = open("demofile.txt", "r")
print(b.read(5))

c = open("demofile.txt", "r")
print(c.readline())
print(c.readline())

d = open("demofile.txt", "r")
for x in d:
    print(x)

e = open("demofile.txt", "r")
print(e.readline())
e.close()