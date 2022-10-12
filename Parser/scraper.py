import requests
from bs4 import BeautifulSoup

url = 'https://www.lamoda.ru/p/mp002xw0b9qb/clothes-masteritsanewclassic-bluza/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('span', class_='js-breadcrumbs__item-text')
for title in titles:
    print(title.text)

print('--------')
url = 'https://www.lamoda.ru/p/mp002xw08rpe/clothes-calvinkleinunderwear-trusy/?promotion_provider_id=display_33_1uFbmSbeZbicRDFNXy5yX1hhNUDAwMlhXMDhSUEU%3D'
response = requests.get(url)
soup = BeautifulSoup(response._content, 'html.parser')
price = soup.find_all('x-product-installment :price=')
# for sku in skus:
#     continue
#     print(sku.text)
print(price)
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
