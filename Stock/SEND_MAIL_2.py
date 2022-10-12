import smtplib
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

import pandas as pd
from pretty_html_table import build_table
current_datetime = datetime.now()

def send_mail(body):
    message = MIMEMultipart()
    message['Subject'] = f"Дефицитные позиции на ЦС КМР на {current_datetime.day}.{current_datetime.month}"
    message['From'] = 'a.dragunov@vistauto.ru'
    #message['Cc'] = "vistparts@vistauto.ru"
    message['To'] = 'a.dragunov@vistauto.ru'

    body_content = body
    message.attach(MIMEText(body_content, "html"))
    msg_body = message.as_string()

    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.login(message['From'], '12345678qaZ')
    server.sendmail(message['From'], message['To'], msg_body)
    server.quit()


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
    column_names = ['Part_no', 'part_name_rus', 'stock_mc1', 'stock', 'free_stock', 'ABC_GROUP', 'total_sales']

    queryset = f"""SELECT kmr_dayly.part_no, kmr_dayly.part_name_rus, kmr_dayly.stock_mc1, kmr_dayly.stock, vist_daily.free_stock, total_sales.ABC_GROUP, total_sales.total_sales 
    FROM kmr_dayly inner join total_sales ON kmr_dayly.part_no = total_sales.part_no left JOIN vist_daily ON kmr_dayly.part_no = vist_daily.part_no 
    WHERE kmr_dayly.cur_day = '{current_datetime.day}' And kmr_dayly.cur_month = '{current_datetime.month}' And kmr_dayly.stock < (total_sales.total_sales * 10) order by total_sales.ABC_GROUP, total_sales.total_sales desc;"""
    df = postgresql_to_dataframe(conn, queryset, column_names)
    return df


def send_country_list():
    gdp_data = get_gdp_data()

    output = build_table(gdp_data, 'yellow_dark', font_size='8px', font_family='Open Sans', text_align='leftr',
                         width='auto', width_dict=['auto', '450px', 'auto', 'auto', 'auto', 'auto', 'auto'],
                         index=False)
    send_mail(output)
    return "Mail sent successfully."


send_country_list()
