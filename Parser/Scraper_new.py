import psycopg2
import requests
from bs4 import BeautifulSoup

i = 0
b = []
url = 'https://www.lamoda.ru/p/ix001xw01bx9/clothes-bershka-dzhinsy/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('span', class_='js-breadcrumbs__item-text')
for title in titles:
    b.append(title.text)
    print(b[i])
    i += 1
    # print(title.text)
try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="111",
                                  host="localhost",
                                  port="5432",
                                  database="Clothes")
    cursor = connection.cursor()
    insert_query = """ INSERT INTO clothes_clothes (link, title, gender, type_clothes, class_clothes, name_clothes, sub_name_clothes, link_picture1, link_picture2 ) VALUES ('url', 'b[0]', 'b[1]', 'b[2]', 'b[3]', 'b[4]', 'b[5]', '', '');"""

    #insert_query2 = """ SELECT * FROM public.clothes_clothes ORDER BY id ASC; """
    cursor.execute(insert_query)
    #print(insert_query2)
    connection.commit()
finally:
    if connection:
        cursor.close()
        connection.close()

print('--------')
url = 'https://www.lamoda.ru/p/mp002xw08rpe/clothes-calvinkleinunderwear-trusy/?promotion_provider_id=display_33_1uFbmSbeZbicRDFNXy5yX1hhNUDAwMlhXMDhSUEU%3D'
response = requests.get(url)
soup = BeautifulSoup(response._content, 'html.parser')
price = soup.find_all('x-product-installment :price=')
# for sku in skus:
#     continue
#     print(sku.text)
# print(price)
print('=======')
a = 0
url = 'https://www.lamoda.ru/p/mp002xw08rpe/clothes-calvinkleinunderwear-trusy/?promotion_provider_id=display_33_1uFbmSbeZbicRDFNXy5yX1hhNUDAwMlhXMDhSUEU%3D'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
srcs = soup.find_all('span', class_='ii-product__attribute-value')
for src in srcs:
    a = (src.text)
print(a)

# urls = []
# len = (soup.find_all('div', class_='x-product-gallery'))
# print(len)
# print('______')
# sub_len = soup.find_all('//a.lmcdn.ru*.jpg')
# print(sub_len)

# for h in soup.find_all('div', class_='x-product-gallery'):
#     urls.append(h.find('a').attrs['src'])
