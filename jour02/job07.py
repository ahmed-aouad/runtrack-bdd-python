import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ouarda2017",
    database="laplateforme",
)

cursor=mydb.cursor()

cursor.execute("SELECT employe.id, employe.nom, employe.prenom, employe.salaire,service.nom from employe inner join service on employe.id_service = service.id")
resultat = cursor.fetchall()
print(resultat)


        