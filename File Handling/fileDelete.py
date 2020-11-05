import os
os.remove("demofile.txt")

# checking first
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# delete folder
os.rmdir("myfolder")
# only remove empty folder