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

first_name = input('What is your first name? ')
last_name = input('What is your last name?')
city = input("What is your city? ")
state = input("What is your state? ")

sql_string = f"INSERT INTO owners(first_name, last_name, city, state) VALUES('{first_name}','{last_name}','{city}','{state}')"
print(f'Your name is {first_name} {last_name} and you live in {city}, {state}')
print(sql_string)
cursor.execute(sql_string)
connection.commit()
cursor.execute("Select * From owners")
print(cursor.fetchall())