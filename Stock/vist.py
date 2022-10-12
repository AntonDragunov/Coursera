import psycopg2

database = psycopg2.connect(database="Nokian", user="postgres", password="111", host="localhost", port="5432")

cursor = database.cursor()

query = """INSERT INTO vist_daily (
            PART_NO,
            free_stock)
             VALUES ('dfdfsdfsdfsdf', '111122121')"""
cursor.execute(query)

cursor.close()

database.commit()

database.close()

print("I just imported Excel into postgreSQL")
