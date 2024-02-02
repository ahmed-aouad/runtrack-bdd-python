import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ouarda2017",
    database="laplateforme",
)

cursor=mydb.cursor()

cursor.execute("SELECT capacite FROM salle")

capacite_total = 0
for capacite in cursor:
    print(capacite)
    capacite_total += capacite[0]

print(f"La capacité de toute les salles est de {capacite_total}")   

mydb.close()
cursor.close()