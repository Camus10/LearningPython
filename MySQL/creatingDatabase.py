import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    # using database
    # database = "from_python"
)
# print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("create databases from_python")

mycursor = mydb.cursor()
mycursor.execute("show databases")
for x in mycursor:
    print(x)