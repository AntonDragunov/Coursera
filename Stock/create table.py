import psycopg2


database = psycopg2.connect(database="Nokian", user="postgres", password="111", host="localhost", port="5432")

cursor = database.cursor()

query = """CREATE TABLE tyre_brands(
            id serial PRIMARY KEY,
            BRAND varchar(200));"""

cursor.execute(query)

cursor.close()

database.commit()

database.close()
