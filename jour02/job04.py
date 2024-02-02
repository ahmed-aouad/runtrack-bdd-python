import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ouarda2017",
    database="laplateforme",
)

cursor=mydb.cursor()

cursor.execute("SELECT nom, capacite FROM salle")

resultat=cursor.fetchall()
print(resultat)

mydb.close()
cursor.close()