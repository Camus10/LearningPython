import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "from_python"
)
mycursor = mydb.cursor()

mycursor.execute("create table customers (name varchar(255), address varchar(255))")