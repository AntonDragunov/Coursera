import requests
from bs4 import BeautifulSoup
a = '04E115561E'
url = 'https://exist.ru/Price/?pcode=04E115561H'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# titles = soup.find_all('span', class_='price')
# for title in titles:
#     print(title.text)


r = requests.get(url)
print(r.status_code)
print(url)
print(r.text)