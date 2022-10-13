import psycopg2


database = psycopg2.connect(database="Nokian", user="postgres", password="111", host="localhost", port="5432")

cursor = database.cursor()

query = """CREATE TABLE partition_dayly_m(
            id serial PRIMARY KEY,
            PART_NO varchar(100),
            PART_NAME varchar(200),
            BRAND varchar(100),
            price numeric(10,3),
            free_stock numeric(10,3),
            time_period numeric(10,3));"""

cursor.execute(query)

cursor.close()

database.commit()

database.close()
