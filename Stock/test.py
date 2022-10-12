import psycopg2
import xlrd
from datetime import datetime

book = xlrd.open_workbook("report.xls")
sheet = book.sheet_by_name("Products")
current_datetime = datetime.now()
database = psycopg2.connect(database="Nokian", user="postgres", password="111", host="localhost", port="5432")

cursor = database.cursor()

query = """INSERT INTO nokian_dayly (partnumber, brand, standard_size, tyre_model, diameter, width, height, seasons, studded, runflat, name_contract, price, price_prepaid, quantity_msk_sod, quantity_pet_svd, cur_year, cur_month, cur_day) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

for r in range(1, sheet.nrows):
    partnumber = sheet.cell(r, 0).value
    brand = sheet.cell(r, 1).value
    standard_size = sheet.cell(r, 2).value
    tyre_model = sheet.cell(r, 3).value
    diameter = sheet.cell(r, 4).value
    width = sheet.cell(r, 5).value
    height = sheet.cell(r, 6).value
    seasons = sheet.cell(r, 7).value
    studded = sheet.cell(r, 8).value
    runflat = sheet.cell(r, 9).value
    name_contract = sheet.cell(r, 10).value
    price = sheet.cell(r, 11).value
    price_prepaid = sheet.cell(r, 12).value
    quantity_msk_sod = sheet.cell(r, 13).value
    quantity_pet_svd = sheet.cell(r, 14).value
    cur_year = 2023#current_datetime.year
    cur_month = 12#current_datetime.month
    cur_day = 85#current_datetime.day
    values = (
    partnumber, brand, standard_size, tyre_model, diameter, width, height, seasons, studded, runflat, name_contract,
    price, price_prepaid, quantity_msk_sod, quantity_pet_svd, cur_year, cur_month, cur_day)

    cursor.execute(query, values)

cursor.close()

database.commit()

database.close()

columns = str(sheet.ncols)
rows = str(sheet.nrows)
# print("I just imported Excel into postgreSQL")
