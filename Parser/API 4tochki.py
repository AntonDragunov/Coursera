from collections import OrderedDict

import requests
from bs4 import BeautifulSoup

params = {'login': 'sa30716', 'password': 's4ktKFX-pN', 'code_list': ['774942']}
response = requests.get("http://api-b2b.4tochki.ru/WCF/ClientService.svc?wsdl", params=params)
print(response.text)
#sa30716
#s4ktKFX-pN

# Документация модуля Zeep
# https://python-zeep.readthedocs.io/en/master/

from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Settings, Client  # pip install zeep
from zeep.transports import Transport


def get_soap():
    """Возвращает данные сервиса"""
    wsdl = 'http://api-b2b.4tochki.ru/WCF/ClientService.svc?wsdl'
    user = "sa30716"
    password = "s4ktKFX-pN"

    settings = Settings(
        strict=True  # строгая обработка запроса
        # raw_response=True  # ответ без обработки lxml-модулем
        # force_https=False
        # xml_huge_tree=True  # ограничение глубины xml-дерева
        # forbid_dtd=True
        # forbid_entities=False
        # xsd_ignore_sequence_order=True
    )

    session = Session()
    session.auth = HTTPBasicAuth(user, password)  # Авторизация через HTTP

    client = Client(
        wsdl=wsdl,
        settings=settings,
        transport=Transport(session=session)
    )

    request = client.service.GetGoodsInfo(**params)
    print(request)
    #result = eval(request)  # Предобразование строки в список словарей
    #data = request.json()
    return


get_soap()

