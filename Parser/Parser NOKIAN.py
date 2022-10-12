import os
from lib2to3.pgen2 import driver
from os.path import basename
from urllib.parse import urlsplit

import requests
import urllib.error
from urllib.request import urlopen

from requests import request

url = 'https://egate.nokiantyres.com/wholesale-ru/'

# Важно. По умолчанию requests отправляет вот такой
# заголовок 'User-Agent': 'python-requests/2.22.0 ,  а это приводит к тому , что Nginx
# отправляет 404 ответ. Поэтому нам нужно сообщить серверу, что запрос идет от браузера

user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

# Создаем сессию и указываем ему наш user-agent
session = requests.Session()
r = session.get(url, headers={
    'User-Agent': user_agent_val
})

# Указываем referer. Иногда , если не указать , то приводит к ошибкам.
session.headers.update({'Referer': url})

# Хотя , мы ранее указывали наш user-agent и запрос удачно прошел и вернул
# нам нужный ответ, но user-agent изменился на тот , который был
# по умолчанию. И поэтому мы обновляем его.
session.headers.update({'User-Agent': user_agent_val})

# Получаем значение _xsrf из cookies
_xsrf = session.cookies.get('_xsrf', domain=".nokiantyres.com")

# Осуществляем вход с помощью метода POST с указанием необходимых данных
post_request = session.post(url, {
    'backUrl': 'https://egate.nokiantyres.com/wholesale-ru/ru/my-account/warehouses',
    'username': 'a.dragunov@vistauto.ru',
    'password': 'WL6k342F8',
    '_xsrf': _xsrf,
    'remember': 'yes',
})


post_request2 = session.post(url, {
    'backUrl': 'https://egate.nokiantyres.com/wholesale-ru/ru/my-account/report.xls',
    'username': 'a.dragunov@vistauto.ru',
    'password': 'WL6k342F8',
    '_xsrf': _xsrf,
    'remember': 'yes',
})
url2 = 'https://egate.nokiantyres.com/wholesale-ru/ru/my-account/report.xls'

response = requests.get(url2)
data = response.content
#https://egate.nokiantyres.com/wholesale-ru/ru/my-account/warehouses


#destination = 'report'
#url_file = 'https://egate.nokiantyres.com/wholesale-ru/ru/my-account/warehouses'
#urllib.request.urlretrieve(url_file, destination)

# Вход успешно воспроизведен и мы сохраняем страницу в html файл
with open("nokian_success.xls", "w", encoding="utf-8") as f:
     f.write(post_request2.text)
#
# from urllib.request import urlopen
# url3 = 'https://egate.nokiantyres.com/wholesale-ru/ru/my-account/report.xls'
# response = urlopen(url3)
# print(response.headers.get_filename())



