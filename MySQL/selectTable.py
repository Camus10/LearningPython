import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "from_python"
)
mycursor = mydb.cursor()

# get all
mycursor.execute("select * from customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# get only 1
mycursor.execute("select * from customers")
myresult = mycursor.fetchone()
print(myresult)