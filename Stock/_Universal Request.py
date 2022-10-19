import time
from datetime import datetime
import shutil
import sys

import numpy as np
import pandas as pd
import psycopg2

# -------------------ВЫБОРКА ТОЛЬКО НУЖНЫХ ПРОИЗВОДИТЕЛЕЙ---------------------------------------------------
tyre_brands = ('BFGoodrich', 'Kormoran', 'Dunlop JP', 'Viatti',
               'Hankook', 'Goodyear', 'Nokian Tyres', 'Matador', 'Continental', 'Yokohama', 'Marshal', 'Michelin',
               'MICHELIN', 'HANKOOK', 'YOKOHAMA', 'GOODYEAR', 'TRIANGLE', 'NEXEN', 'PIRELLI', 'VIATTI', 'КАМА',

               'Pirelli', 'Bridgestone', 'BRIDGESTONE', 'Kama', 'Nexen', 'Gislaved', 'Toyo', 'Nitto', 'Doublestar',
               'Formula',
               'Cordiant', 'Vredestein', 'GT Radial', 'Triangle', 'Maxxis', 'GiTi', 'Altenzo', 'Ovation', 'Compasal',
               'Mickey Thompson', 'Sava', 'Sunfull', 'Onyx', 'Cachland', 'Sailun', 'HiFly', 'Roadcruza', 'NOKIAN',
               'Nordman', 'PIRELLI 2')

non_sale_brands = ('MIRKA', 'Mirka/Mirlontotal', 'festol', 'Festool', 'не указан', 'HYDRONIC', 'SERVISEZAP', 'RADEX',
                   'DuPont', 'Sunmight', '------------', 'Shell', 'TOTAL', 'LIQUI MOLY', 'VAG', 'SKODA', 'MRK', '3 M',
                   '3',
                   'Menzerna', 'TESLA', 'TESLA (ПРЕДОХРАНИТЕЛИ И ПРОВОД', 'VOLZE', 'U-POL', 'Upol', 'Sunmight',
                   'RoxelPro', 'GLASS', 'Forch', 'Duxone', 'Cromax (DuPont)', 'Car System', 'BlackFox', '3M',
                   'VAG / AUDI / PORSCHE / SKODA',
                   'STP (STANDARTPLAST)', 'SGM', 'SGM SAAB', 'Неизвестный производитель', 'HELLA', 'G-Power', 'LAVR',
                   'Camelion', 'minamoto', 'ZALMER', 'Автомоторс', 'Alu-frost', 'KOVAX', 'Россия', 'Орехово-Зуево',
                   'CARSYSTEM')

current_time_temp = time.localtime()
current_time = f'{current_time_temp.tm_hour}_{current_time_temp.tm_min}_{current_time_temp.tm_sec}'
current_datetime = datetime.now()
current_date = f'{current_datetime.day}.{current_datetime.month}.{current_datetime.year}'
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

current_file_name = 'Vist_Avto_stock' + ' ' + str(current_datetime.day) + '_' + str(current_datetime.month) + '_' + str(
	current_datetime.year)

yandex = f'marketplace-stock YAM {current_date}-{current_time}.xlsx'
kia_tyre = f'{current_file_name}-{current_time}_tyre.xlsx'

query = f"""select partition_dayly.part_no, partition_dayly.free_stock, partition_dayly.part_name,
                                partition_dayly.price AS price, partition_dayly.brand, partition_dayly.time_period
                                from public.partition_dayly
                                join vist_daily ON partition_dayly.part_no = vist_daily.part_no
                                 WHERE brand in {tyre_brands};"""

query_nelikvid = f"""select partition_dayly.part_no, partition_dayly.free_stock, partition_dayly.part_name,
                                partition_dayly.price AS price, partition_dayly.brand, partition_dayly.time_period
                                from public.partition_dayly
                                join vist_daily ON partition_dayly.part_no = vist_daily.part_no;"""


column_names2 = ['Part_no', 'free_stock', 'part_name_rus',  'price', 'brand', 'time_period']
df2 = postgresql_to_dataframe(conn, query_nelikvid, column_names2)
with open(f'Price_to_email/Неликвид КИА.xlsx', "w+") as f:
	df2.to_excel(f'Price_to_email/Неликвид КИА.xlsx', index=False)





df4 = postgresql_to_dataframe(conn, query, column_names2)
df4['free_stock'] = df4['free_stock'].astype(str)
df4['free_stock'] = pd.to_numeric(df4['free_stock']).astype(int)
df4['time_period'] = df4['time_period'].astype(str)
df4['time_period'] = df4['time_period'].str.replace('.', ',', regex=True)
df4['price'] = df4['price'].astype(str)
df4['price'] = df4['price'].str.replace('.', ',', regex=True)

df4.insert(1, "пустой столбец", np.nan)
print(df4)
my_file2 = open(f'Price_to_email/{kia_tyre}', "w+")
df4.to_excel(f'Price_to_email/{kia_tyre}', index=False)
my_file2.close()

df_yandex = df4.drop(['part_name_rus',  'price', 'brand', 'time_period'], axis=1)







try:
	shutil.copyfile(rf'Price_to_email/marketplace-stock YAM.xlsx', rf'Price_to_email/{yandex}')
except:
	print('ФАЙЛ НЕ СКОПИРОВАН ПО КАКИМ-ТО ПРИЧИНАМ')

with pd.ExcelWriter(f'Price_to_email/{yandex}',mode='a', if_sheet_exists='overlay') as writer:
	df_yandex.to_excel(writer, sheet_name='Остатки', header=False, index=False, startrow=2, startcol=1)





# try:
# 	shutil.copyfile(rf'Price_to_email/{kia_tyre}', rf'\\192.168.10.117\kia\ПРАЙС\{kia_tyre}.xlsx')
# except:
# 	print('недоступна конечная директория либо проблема с файлом по ШИНАМ!')

try:
	shutil.copyfile(rf'Price_to_email/{yandex}', rf'\\192.168.10.117\kia\ПРАЙС\{yandex}')
except:
	print('недоступна конечная директория либо проблема с файлом по ШИНАМ ЯНДЕКС НАЛИЧИЕ!')