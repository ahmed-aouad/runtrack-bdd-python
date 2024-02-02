import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ouarda2017",
    database="laplateforme",
)

cursor=mydb.cursor()

cursor.execute("SELECT superficie FROM etage")

superficie_total = 0

for superficie in cursor:
    superficie_total += superficie[0]

print(f"La superficie de la plateforme est de {superficie_total} m²")   

mydb.close()
cursor.close()