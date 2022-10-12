import psycopg2
import xlrd
from datetime import datetime

database = psycopg2.connect(database="Nokian", user="postgres", password="111", host="localhost", port="5432")

cursor = database.cursor()

query = """CREATE TABLE kmr_dayly(
            id serial PRIMARY KEY,
            PART_NO varchar(100),
            ITC_CODE varchar(100),
            ITC_PART varchar(100),
            MODEL varchar(100),
            PART_NAME_ENG varchar(100),
            PART_NAME_RUS varchar(100),
            MPQ1 numeric(10,2),
            D_ORDER_DNP numeric(10,2),
            LIST_PRICE numeric(10,2),
            STOCK_MC1 integer,
            STOCK_ME1 integer,
            STOCK_MN1 integer,
            STOCK_MS1 integer,
            STOCK_MK1 integer,
            STOCK integer,
            cur_year integer,
            cur_month integer,
            cur_day integer);"""

cursor.execute(query)

cursor.close()

database.commit()

database.close()
