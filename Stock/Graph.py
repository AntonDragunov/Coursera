from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

# width = 0.4
import pandas as pd
from matplotlib.ticker import MultipleLocator, NullLocator

current_datetime = datetime.now()


# x_list = list(range(0, 5))
# y1_list = [22, 33, 44, 22, 19]
# # x_indexers = np.arrange(len(x_list))
#
#
# plt.plot(x_list, y1_list)
# plt.show()


def get_gdp_data():
    import sys
    import psycopg2

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
    column_names = ['Part_no', 'part_name_rus', 'd_order_dnp', 'stock', 'cur_month and cur_day']
    partnumber = '2630035505'

    # 2630035505
    queryset = f"""SELECT part_no, part_name_rus, d_order_dnp, stock, cur_day from kmr_dayly WHERE PART_NO = '{partnumber}' AND cur_month > '{current_datetime.month}'-1 order by cur_month desc, cur_day desc"""
    # queryset = f"""SELECT part_no, part_name_rus, d_order_dnp, stock, cur_day||'.'||cur_month from kmr_dayly WHERE PART_NO ='{partnumber}' order by cur_month desc, cur_day desc"""
    df = postgresql_to_dataframe(conn, queryset, column_names)
    date = []
    stock_a_day = []

    partname = ''
    for x in df["part_name_rus"]:
        partname = x
        new_part_name = partname.rstrip()
        break

    for x in df["stock"]:
        stock_a_day.append(x)

    for y in df["cur_month and cur_day"]:
        date.append(y)

    draw_plot(date, stock_a_day, partnumber, new_part_name)
    return df


def draw_plot(data, stock, partnumber, new_part_name):
    data.reverse()
    stock.reverse()
    fig = plt.figure()
    ax = fig.add_subplot()
    fig.suptitle(f'{partnumber} - {new_part_name}')
    plt.xlim(0, len(data))

    plt.plot(data, stock)

    plt.grid()

    plt.show()


gdp_data = get_gdp_data()
