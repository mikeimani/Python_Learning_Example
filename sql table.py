import psycopg2
connection = psycopg2.connect(user = "postgres",
				password = "Feuille1",
				host = "127.0.0.1",
				port = "5432",
				database = "pet_owner")
cursor = connection.cursor()
cursor.execute("Select * From pets")
table_list = cursor.fetchall()
print (table_list)

print(table_list[2])

print(table_list[2][2])

