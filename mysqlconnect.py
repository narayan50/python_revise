import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",   
    user="root",
    password="qwerty",
    database="cars"
)

mycursor = myconn.cursor()
sql = "SELECT * FROM carinfo"