import psycopg2
import xlrd
from config import host, user, db_name, password

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT part_no, part_name_rus, d_order_dnp, stock, cur_month, cur_day from kmr_dayly WHERE
             PART_NO = '2630035505' order by cur_month desc, cur_day desc;""")
        print(cursor.fetchall())

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
