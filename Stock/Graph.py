from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
from matplotlib.ticker import MultipleLocator, IndexLocator

current_datetime = datetime.now()


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
    partnumber = '86640F1500'

    # 2630035505
    queryset = f"""SELECT part_no, part_name_rus, d_order_dnp, stock, cur_day from kmr_dayly WHERE PART_NO = '{partnumber}' AND cur_month > '{current_datetime.month}'-1 order by cur_month desc, cur_day desc"""

    df_1 = postgresql_to_dataframe(conn, queryset, column_names)
    queryset2 = f"""SELECT part_no, part_name_rus, d_order_dnp, stock, cur_day||'.'||cur_month from kmr_dayly WHERE PART_NO ='{partnumber}' order by cur_month desc, cur_day desc"""
    df_2 = postgresql_to_dataframe(conn, queryset2, column_names)
    print(df_2)
    print()
    print(df_1)
    date = []
    date2 = []
    stock_a_day = []
    stock_a_day2 = []

    # partname = ''
    for x in df_1["part_name_rus"]:
        partname = x
        new_part_name = partname.rstrip()
        break

    for x in df_1["stock"]:
        stock_a_day.append(x)
    for y in df_2["stock"]:
        stock_a_day2.append(y)

    for z in df_1["cur_month and cur_day"]:
        date.append(z)
    for r in df_2["cur_month and cur_day"]:
        date2.append(r)

    print(len(date2))
    print(len(stock_a_day2))

    draw_plot(date, date2, stock_a_day, stock_a_day2, partnumber, new_part_name)
    # return df


def draw_plot(data, data2, stock, stock2, part_number, newpartname):
    data.reverse()
    stock.reverse()
    data2.reverse()
    stock2.reverse()
    fig = plt.figure()
    ax_1 = fig.add_subplot(2, 1, 1)
    ax_2 = fig.add_subplot(3, 1, 3)
    fig.suptitle(f'{part_number} - {newpartname}')
    # plt.xlim(0, len(data))
    # plt.xlabel('день текущего месяца')
    # plt.ylabel('количество, шт')
    ax_1.set(title='за весь период')
    ax_2.set(title='текущий месяц', xticks=data, yticks=stock)
    plt.grid()
    ax_1.xaxis.set_major_locator(IndexLocator(base=30, offset=0))
    # ax_1.xaxis.set_major_locator(MultipleLocator(base=30))
    ax_2.xaxis.set_major_locator(MultipleLocator(base=5))
    ax_2.yaxis.set_major_locator(MultipleLocator(base=10))
    ax_1.plot(data2, stock2)
    ax_2.plot(data, stock)
    plt.show()


gdp_data = get_gdp_data()
