import sys

import pandas as pd
import psycopg2

# -------------------ВЫБОРКА ТОЛЬКО НУЖНЫХ ПРОИЗВОДИТЕЛЕЙ---------------------------------------------------
tyre_brands = ('Kia', 'Kormoran', 'Dunlop JP', 'Viatti',
               'Hankook', 'Goodyear', 'Nokian Tyres', 'Matador', 'Continental', 'Yokohama', 'Marshal', 'Michelin',
               'Pirelli', 'Bridgestone', 'Kama', 'Nexen', 'Gislaved', 'Toyo', 'Nitto', 'Doublestar', 'Formula',
               'Cordiant', 'Vredestein', 'GT Radial', 'Triangle', 'Maxxis', 'GiTi', 'Altenzo', 'Ovation', 'Compasal',
               'Mickey Thompson', 'Sava', 'Sunfull', 'Onyx', 'Cachland', 'Sailun', 'HiFly', 'Roadcruza', 'NOKIAN',
               'Nordman', 'PIRELLI 2')


non_sale_brands = ('MIRKA', 'Mirka/Mirlontotal', 'festol', 'Festool', 'не указан', 'HYDRONIC', 'SERVISEZAP', 'RADEX',
 'DuPont', 'Sunmight', '------------', 'Shell', 'TOTAL', 'LIQUI MOLY', 'VAG', 'SKODA', 'MRK', '3 M', '3',
 'Menzerna', 'TESLA', 'TESLA (ПРЕДОХРАНИТЕЛИ И ПРОВОД', 'VOLZE', 'U-POL', 'Upol', 'Sunmight', 'RoxelPro', 'GLASS',
    'Forch', 'Duxone', 'Cromax (DuPont)', 'Car System', 'BlackFox', '3M', 'VAG / AUDI / PORSCHE / SKODA',
'STP (STANDARTPLAST)', 'SGM', 'SGM SAAB', 'Неизвестный производитель', 'HELLA', 'G-Power', 'LAVR', 'Camelion',
                   'minamoto')

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
column_names = ['Part_no', 'part_name_rus', 'free_stock', 'price', 'brand']

query = f"""select partition_dayly.Part_no, partition_dayly.part_name, vist_daily.free_stock, partition_dayly.price, partition_dayly.brand from partition_dayly
            join vist_daily on vist_daily.part_no = partition_dayly.part_no
                WHERE not brand in {tyre_brands};"""
# for row in worksheet.iter_rows(min_row=2, max_col=2, max_row=None, values_only=True):
#     print(row)
#     values = values + row
df = postgresql_to_dataframe(conn, query, column_names)
print(df)
