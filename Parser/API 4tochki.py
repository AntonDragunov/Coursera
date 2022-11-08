from collections import OrderedDict

import requests
from bs4 import BeautifulSoup

params = {'login': 'sa30716', 'password': 's4ktKFX-pN', 'code_list': ['R1147']}
params2 = {'login': 'sa30716', 'password': 's4ktKFX-pN', 'orderNumber': 'F8546660'}

orderProducts = {"code" : 'R1147', "quantity" : 1, "wrh" : 1}
params3 = {'login': 'sa30716', 'password': 's4ktKFX-pN', 'order': f'{orderProducts}'}
params4 = {'login': 'sa30716', 'password': 's4ktKFX-pN'}
params5 = {'login': 'sa30716', 'password': 's4ktKFX-pN', 'marka': 'CHERY'}
params6 = {'login': 'sa30716', 'password': 's4ktKFX-pN', 'marka': 'CHERY', 'model' : 'Tiggo 4','year_beg' : 2020 ,
            'year_end' : 2022}
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

    request = client.service.GetGoodsInfo(**params) #получение информация по артикулу
    request2 = client.service.GetOrderInfo(**params2) #получение информации по заказу
    #request3 = client.service.CreateOrder(**params3)
    request4 = client.service.GetMarkaAvto(**params4)
    request5 = client.service.GetModelAvto(**params5)
    request6 = client.service.GetModificationAvto(**params6)
    
    
    
    print(request)
    print(...)
    print(request2)
    print(request4)
    print(request5)
    print(request6)
    #result = eval(request)  # Предобразование строки в список словарей
    #data = request.json()
    return


get_soap()

