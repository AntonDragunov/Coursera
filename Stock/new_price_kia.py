from datetime import datetime

from email.header import Header

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
                   'CARSYSTEM')


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
	
	# """select partition_dayly.part_no, partition_dayly.part_name,
	#                     CASE WHEN (partition_dayly.free_stock) > 20 THEN 5
	#                     WHEN (partition_dayly.free_stock) > 3 THEN 3
	#                     ELSE partition_dayly.free_stock
	#                     END AS free_stock,
	#                     CASE WHEN (partition_dayly.time_period) < 3 THEN round(kmr_dayly.d_order_dnp * 1.2 * 1.30, 0)
	#                      WHEN (partition_dayly.time_period) > 12 THEN round(partition_dayly.price, 0)
	#                       ELSE
	#
	#
	#
	#
	#                       round(kmr_dayly.d_order_dnp * 1.2 * 1.02, 0)
	#                        END AS price,
	#                         partition_dayly.brand from public.partition_dayly
	#                         join kmr_dayly ON partition_dayly.part_no = kmr_dayly.part_no
	#                         join vist_daily ON partition_dayly.part_no = vist_daily.part_no
	#                          WHERE kmr_dayly.cur_day = '{current_datetime.day}' And kmr_dayly.cur_month = '{current_datetime.month}'
	#                           And kmr_dayly.stock > 0;"""
	
	queryset = f"""select partition_dayly.part_no, partition_dayly.part_name,
                    CASE WHEN (partition_dayly.free_stock) > 20 THEN 10
                    WHEN (partition_dayly.free_stock) > 3 THEN 8
                    ELSE partition_dayly.free_stock
                    END AS free_stock,    
                    CASE WHEN (partition_dayly.time_period) < 3 THEN round(kmr_dayly.d_order_dnp * 1.2 * 1.21, 0)
                     WHEN (partition_dayly.time_period) > 12 THEN round(partition_dayly.price, 0)
                      ELSE 
                      (CASE WHEN (kmr_dayly.d_order_dnp * 1.2) > 30000 THEN round(partition_dayly.price * 1.01, 0)
                        WHEN (kmr_dayly.d_order_dnp * 1.2) > 750 THEN round(partition_dayly.price * 1.13, 0)
                        ELSE round(kmr_dayly.d_order_dnp * 1.2 * 1.55, 0) END)
                       END AS price,
                        partition_dayly.brand from public.partition_dayly
                        join kmr_dayly ON partition_dayly.part_no = kmr_dayly.part_no
                        join vist_daily ON partition_dayly.part_no = vist_daily.part_no
                         WHERE kmr_dayly.cur_day = '{current_datetime.day}' And kmr_dayly.cur_month = '{current_datetime.month}'
                          And kmr_dayly.stock > 0;"""
	df = postgresql_to_dataframe(conn, queryset, column_names)
	print(df)
	queryset2 = f"""select partition_dayly.part_no, partition_dayly.part_name, partition_dayly.free_stock,
                        partition_dayly.price AS price, partition_dayly.brand from public.partition_dayly
                         FULL OUTER join kmr_dayly ON partition_dayly.part_no = kmr_dayly.part_no
                         join vist_daily ON partition_dayly.part_no = vist_daily.part_no
                         WHERE kmr_dayly.cur_day = '{current_datetime.day}' 
                         And kmr_dayly.cur_month = '{current_datetime.month}' And kmr_dayly.stock = 0
                          And partition_dayly.time_period > 6 And Not brand in {non_sale_brands};"""
	queryset3 = f"""select partition_dayly.part_no, partition_dayly.part_name, partition_dayly.free_stock,
                            partition_dayly.price AS price, partition_dayly.brand from public.partition_dayly
                            join vist_daily ON partition_dayly.part_no = vist_daily.part_no
                             WHERE partition_dayly.time_period > 2
                             And Not brand in {tyre_brands} And Not brand in {non_sale_brands}
                             And partition_dayly.brand Not Like 'Kia';"""
	# And partition_dayly.brand Not Like 'Kia'  - вырезал окончание из df3
	queryset4 = f"""select partition_dayly.part_no, partition_dayly.part_name, partition_dayly.free_stock,
                                partition_dayly.price AS price, partition_dayly.brand, partition_dayly.time_period
                                from public.partition_dayly
                                join vist_daily ON partition_dayly.part_no = vist_daily.part_no
                                 WHERE partition_dayly.time_period > 6 And brand in {tyre_brands};"""
	df2 = postgresql_to_dataframe(conn, queryset2, column_names)
	print(df2)
	df3 = postgresql_to_dataframe(conn, queryset3, column_names)
	print(df3)
	column_names2 = ['Part_no', 'part_name_rus', 'free_stock', 'price', 'brand', 'time_period']
	df4 = postgresql_to_dataframe(conn, queryset4, column_names2)
	print(df4)
	# current_file_name = 'Exist наличие КИА' + str(current_datetime.day)
	my_file = open(f'Price_to_email/{current_file_name}.xlsx', "w+")
	# df.to_excel(f'{current_file_name}.xlsx', index=False)
	# my_file.close()
	# my_file = open(f'{current_file_name}.xlsx', "a")
	df_row_concat = pd.concat([df, df2, df3])
	
	df_row_concat.to_excel(f'Price_to_email/{current_file_name}.xlsx', index=False)
	my_file.close()
	my_file2 = open(f'Price_to_email/{current_file_name}_tyre.xlsx', "w+")
	df4.to_excel(f'Price_to_email/{current_file_name}_tyre.xlsx', index=False)
	my_file2.close()


# def send_country_list(current_file_name):
#     gdp_data = get_gdp_data()
#
#     output = build_table(gdp_data, 'yellow_dark', font_size='8px', font_family='Open Sans', text_align='leftr',
#                          width='auto', width_dict=['auto', '450px', 'auto', 'auto', 'auto', 'auto', 'auto'],
#                          index=False)
#     send_mail(output, current_file_name)
#
#     return "Mail sent successfully."
#
# def send_mail2(body, current_file_name):
#     message = MIMEMultipart()
#     message['Subject'] = 'e_kiavist'
#     message['From'] = 'a.dragunov@vistauto.ru'
#     #message['Cc'] = "vistparts@vistauto.ru"
#     message['To'] = 'a.dragunov@vistauto.ru'
#
#     body_content = body
#     #message.attach(MIMEText(body_content, "html"))
#
#
#     #message.attach(MIMEText(body_content, 'plain'))
#     # attach_file_name = f'{current_file_name}.xlsx'
#     # attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
#     # payload = MIMEBase('application', 'octate-stream')
#     # payload.set_payload((attach_file).read())
#     # encoders.encode_base64(payload)  # encode the attachment
#     # # add payload header with filename
#     # payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
#     # message.attach(payload)
#     #msg_body = message.as_string()
#     message.attach(MIMEText(body_content))
#
#
#
#
#     server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
#     server.login(message['From'], '12345678qaZ')
#     server.sendmail(message['From'], message['To'], msg_body)
#     server.quit()
current_file_name = 'Vist_Avto_stock' + ' ' + str(current_datetime.day) + '_' + str(current_datetime.month) + '_' + str(
	current_datetime.year)

"===============================================функция отправки письма с вложением========================================="


def send_email(addr_to, msg_subj, msg_text, files):
	addr_from = "a.dragunov@vistauto.ru"  # Отправитель
	password = "12345678qaZ"  # Пароль
	
	msg = MIMEMultipart()  # Создаем сообщение
	msg['From'] = "a.dragunov@vistauto.ru"  # Адресат
	msg['To'] = addr_to  # Получатель
	msg['Cc'] = "a.dragunov@vistauto.ru"  # COPY
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
	f'Price_to_email/{current_file_name}.xlsx']  # Если нужно отправить все файлы из заданной папки, нужно указать её
files2 = [f'Price_to_email/{current_file_name}_tyre.xlsx']
get_gdp_data()
send_email(addr_to, "e_kiavist", "", files)
send_email(addr_to2,
           f'Шины в неликвиде в КИА на {current_datetime.day}.{current_datetime.month}.{current_datetime.year}',
           "", files2)