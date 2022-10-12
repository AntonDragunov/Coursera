import psycopg2

database = psycopg2.connect(database="Nokian", user="postgres", password="111", host="localhost", port="5432")

cursor = database.cursor()
query = """SELECT * from kmr_dayly WHERE PART_NO = '2630035505';"""
print(cursor.fetchone())
# cursor.execute(query)
# print(query)

cursor.close()

database.commit()

database.close()

print("I just imported Excel into postgreSQL")
