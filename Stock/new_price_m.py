from datetime import datetime

from email.header import Header

import numpy as np
import pandas as pd

current_datetime = datetime.now()

import smtplib  # Импортируем библиотеку по работе с SMTP
import os  # Функции для работы с операционной системой, не зависящие от используемой операционной системы

# Добавляем необходимые подклассы - MIME-типы
import mimetypes  # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
from email import encoders  # Импортируем энкодер
from email.mime.base import MIMEBase  # Общий тип
from email.mime.text import MIMEText  # Текст/HTML
from email.mime.image import MIMEImage  # Изображения
from email.mime.audio import MIMEAudio  # Аудио
from email.mime.multipart import MIMEMultipart
import shutil
import email
import os

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
                   'CARSYSTEM', 'MOBIL', 'BARDAHL', 'ENEOS', 'TOTACHI', 'Nordberg', 'Fagumit', 'GLEID', 'Osram',
                   'ПРИМ', 'Лукойл', 'GreenCool', 'Ravenol', 'IDEMITSU', 'ERRECOM', 'CASTROL', 'OILRIGHT', 'NGN')


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
	column_names = ['Part_no', 'part_name_rus', 'free_stock', 'price', 'brand']
	
	queryset_m = f"""select partition_dayly_m.part_no, partition_dayly_m.part_name, partition_dayly_m.free_stock,
	
	          CASE WHEN partition_dayly_m.time_period < 3 THEN round(partition_dayly_m.price * 1.25, 0)
                     WHEN partition_dayly_m.time_period > 12 THEN round(partition_dayly_m.price * 0.95, 0)
                      ELSE round(partition_dayly_m.price * 1.001, 0)
                        END AS price,
	                
				partition_dayly_m.brand
	            from public.partition_dayly_m
	                join vist_daily_m ON partition_dayly_m.part_no = vist_daily_m.part_no
	                    WHERE Not partition_dayly_m.part_name iLIKE '%жидкость%'
	                    and Not partition_dayly_m.part_name iLIKE '%масло%' and not brand in {non_sale_brands}
	                    and not brand in {tyre_brands} And partition_dayly_m.price > 500;"""
	df = postgresql_to_dataframe(conn, queryset_m, column_names)

	
	print(df)
	
	# column_names2 = ['Part_no', 'free_stock', 'part_name_rus', 'price', 'brand', 'time_period']
	# df4 = postgresql_to_dataframe(conn, queryset4, column_names2)
	# df4['free_stock'] = df4['free_stock'].astype(str)
	# df4['free_stock'] = df4['free_stock'].str.replace('.', ',', regex=True)
	# df4.insert(1, "пустой столбец", np.nan)
	#
	# my_file = open(f'Price_to_email/{current_file_name}.xlsx', "w+")
	#
	# df_row_concat = pd.concat([df, df2, df3])
	#
	# df_row_concat.to_excel(f'Price_to_email/{current_file_name}.xlsx', index=False)
	# my_file.close()
	my_file2 = open(f'Price_to_email/{current_file_name}_M.xlsx', "w+")
	df.to_excel(f'Price_to_email/{current_file_name}_M.xlsx', index=False)
	my_file2.close()
	try:
		shutil.copyfile(rf'Price_to_email/{current_file_name}_M.xlsx', rf'\\192.168.10.117\kia\ПРАЙС\{current_file_name}_M.xlsx')
	except:
		print('недоступна конечная директория либо проблема с файлом по запчастям MITSUBISHI!')

# try:
# 	shutil.copyfile(rf'Price_to_email/{current_file_name}.xlsx',
# 	                rf'\\192.168.10.117\kia\ПРАЙС\{current_file_name}.xlsx')
# except:
# 	print('недоступна конечная директория либо проблема с файлом по запчастям КИА!')
# try:
# 	shutil.copyfile(rf'Price_to_email/{current_file_name}_tyre.xlsx',
# 	                rf'\\192.168.10.117\kia\ПРАЙС\{current_file_name}_tyre.xlsx')
# except:
# 	print('недоступна конечная директория либо проблема с файлом по ШИНАМ!')


current_file_name = 'Vist_Aktiv_stock' + ' ' + str(current_datetime.day) + '_' + str(
	current_datetime.month) + '_' + str(
	current_datetime.year)

"===============================================функция отправки письма с вложением========================================="


def send_email(addr_to, msg_subj, msg_text, files):
	addr_from = "a.dragunov@vistauto.ru"  # Отправитель
	password = "12345678qaZ"  # Пароль
	
	msg = MIMEMultipart()  # Создаем сообщение
	msg['From'] = "a.dragunov@vistauto.ru"  # Адресат
	msg['To'] = addr_to  # Получатель
	msg['Cc'] = "m.lobanov@vistauto.ru"  # COPY
	msg['Subject'] = msg_subj  # Тема сообщения
	
	body = msg_text  # Текст сообщения
	msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст
	
	process_attachement(msg, files)
	
	# ======== Этот блок настраивается для каждого почтового провайдера отдельно ===============================================
	server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)  # Создаем объект SMTP
	# server.starttls()                                      # Начинаем шифрованный обмен по TLS
	# server.set_debuglevel(True)                            # Включаем режим отладки, если не нужен - можно закомментировать
	server.login(addr_from, password)  # Получаем доступ
	server.send_message(msg)  # Отправляем сообщение
	server.quit()  # Выходим


# ==========================================================================================================================


def process_attachement(msg, files):  # Функция по обработке списка, добавляемых к сообщению файлов
	for f in files:
		if os.path.isfile(f):  # Если файл существует
			attach_file(msg, f)  # Добавляем файл к сообщению
		elif os.path.exists(f):  # Если путь не файл и существует, значит - папка
			dir = os.listdir(f)  # Получаем список файлов в папке
			for file in dir:  # Перебираем все файлы и...
				attach_file(msg, f + "/" + file)  # ...добавляем каждый файл к сообщению


def attach_file(msg, filepath):  # Функция по добавлению конкретного файла к сообщению
	filename = os.path.basename(filepath)  # Получаем только имя файла
	ctype, encoding = mimetypes.guess_type(filepath)  # Определяем тип файла на основе его расширения
	if ctype is None or encoding is not None:  # Если тип файла не определяется
		ctype = 'application/octet-stream'  # Будем использовать общий тип
	maintype, subtype = ctype.split('/', 1)  # Получаем тип и подтип
	if maintype == 'text':  # Если текстовый файл
		with open(filepath) as fp:  # Открываем файл для чтения
			file = MIMEText(fp.read(), _subtype=subtype)  # Используем тип MIMEText
			fp.close()  # После использования файл обязательно нужно закрыть
	elif maintype == 'image':  # Если изображение
		with open(filepath, 'rb') as fp:
			file = MIMEImage(fp.read(), _subtype=subtype)
			fp.close()
	elif maintype == 'audio':  # Если аудио
		with open(filepath, 'rb') as fp:
			file = MIMEAudio(fp.read(), _subtype=subtype)
			fp.close()
	else:  # Неизвестный тип файла
		with open(filepath, 'rb') as fp:
			file = MIMEBase(maintype, subtype)  # Используем общий MIME-тип
			file.set_payload(fp.read())  # Добавляем содержимое общего типа (полезную нагрузку)
			fp.close()
			encoders.encode_base64(file)  # Содержимое должно кодироваться как Base64
	
	mail_coding = 'utf-8'  # Добавляем заголовки
	att_header = Header(os.path.basename(filepath), mail_coding);
	file.add_header('Content-Disposition', 'attachment; filename="%s"' % att_header)
	
	msg.attach(file)  # Присоединяем файл к сообщению


# Использование функции send_email()
addr_to = "Price@exist.ru"  # Получатель
addr_to2 = 'm.lobanov@vistauto.ru'
files = [
	f'Price_to_email/{current_file_name}_M.xlsx']  # Если нужно отправить все файлы из заданной папки, нужно указать её
#files2 = [f'Price_to_email/{current_file_name}.xlsx']
get_gdp_data()
send_email(addr_to, "e_vist", "", files)
# send_email(addr_to2,
#           f'Шины в неликвиде в КИА на {current_datetime.day}.{current_datetime.month}.{current_datetime.year}',
#          "", files2)
