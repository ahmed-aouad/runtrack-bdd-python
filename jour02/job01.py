import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ouarda2017",
    database="laplateforme",
)

cursor=mydb.cursor()

cursor.execute("SELECT * FROM etudiant")

student=cursor.fetchall()
print(student)
