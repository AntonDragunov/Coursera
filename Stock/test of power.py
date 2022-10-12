import sys

import psycopg2
import pandas as pd

# Connection parameters, yours will be different
param_dic = {
    "host": '127.1.0.0',
    "database": 'Nokian',
    "user": 'postgres',
    "password": '111'
}


def connect(params_dic):
    # """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(database="Nokian", user="postgres", password="111", host="localhost", port="5432")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn

def postgresql_to_dataframe(conn, select_query, column_names):
    # """    # Tranform a SELECT query into a pandas dataframe    # """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1
    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()
    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df


conn = connect(param_dic)
column_names = ['Part_no', 'part_name_rus', 'stock_mc1','stock', 'free_stock', 'ABC_GROUP', 'total_sales']

queryset = """SELECT kmr_dayly.part_no, kmr_dayly.part_name_rus, kmr_dayly.stock_mc1, kmr_dayly.stock, vist_daily.free_stock, total_sales.ABC_GROUP, total_sales.total_sales 
FROM kmr_dayly inner join total_sales ON kmr_dayly.part_no = total_sales.part_no left JOIN vist_daily ON kmr_dayly.part_no = vist_daily.part_no 
WHERE kmr_dayly.cur_day = 25 And cur_month = 4 And vist_daily.free_stock is Null order by total_sales.ABC_GROUP, total_sales.total_sales desc;"""

df = postgresql_to_dataframe(conn, queryset, column_names)

