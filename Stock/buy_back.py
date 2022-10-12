import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
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
    column_names2 = ['Part_no']
    queryset2 = f"""SELECT buy_back.part_no from buy_back INNER JOIN kmr_dayly ON buy_back.part_no = kmr_dayly.part_no 
                    WHERE kmr_dayly.cur_day = '{current_datetime.day}' And kmr_dayly.cur_month = '{current_datetime.month}';"""

    df2 = postgresql_to_dataframe(conn, queryset2, column_names2)
    print(df2)
    print('____________________')
    stock_all_number = []
    stock_one_number = []
    for y in df2['Part_no']:
        queryset = f"""SELECT part_no, part_name_rus, d_order_dnp, stock, cur_month||' '||cur_day from kmr_dayly WHERE PART_NO ='{y}' order by cur_month desc, cur_day desc"""
        df = postgresql_to_dataframe(conn, queryset, column_names)
        stock_one_number = []
        for z in df["stock"]:
            stock_one_number.append(z)
        #print(df)
        stock_one_number.insert(0, y)
        stock_all_number.append(stock_one_number)
    #print(stock_all_number)
    df3 = pd.DataFrame(stock_all_number)
    my_file = open('analys_izlishek.xlsx', "w+")
    df3.to_excel('analys_izlishek.xlsx', index=False)
    my_file.close()

    date = []
    stock_a_day = []
    avg_a_week = 0
    list_of_avg_a_day = []
    count = 0
    for x in df["stock"]:
        stock_a_day.append(x)
        avg_a_week += x
        #print(count, avg_a_week, x)
        if count == 6:
            list_of_avg_a_day.append(int(avg_a_week/7))

            avg_a_week = 0
            count = 0
        else:
            count +=1
    list_of_avg_a_day.reverse()
    print(list_of_avg_a_day)
    for y in df["cur_month and cur_day"]:
        date.append(y)

    s = df["stock"].pct_change()
    print(s)


    print(stock_a_day)
    print(date)

    date.reverse()
    stock_a_day.reverse()
    plt.plot(date, stock_a_day)
    plt.show()
    return df




gdp_data = get_gdp_data()