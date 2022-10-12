from collections import OrderedDict

import requests
from bs4 import BeautifulSoup
#
# client = BeautifulSoup("http://api-b2b.4tochki.ru/WCF/ClientService.svc?wsdl");
# params = OrderedDict([('login', 'test'), ('password', 'test'), ('filter', OrderedDict(
#     [('season_list', OrderedDict([(0, 'w')])), ('width_min', 185), ('width_max', 185), ('height_min', 60),
#      ('height_max', 60), ('diameter_min', 15), ('diameter_max', 15)])), ('page', 0)]);
# answer = client.GetFindTyre(params);
# print(answer)


params = {'login': 'sa30716', 'password': 's4ktKFX-pN', 'code_list': ['2329500', 'WHS063930']}
response = requests.get("http://api-b2b.4tochki.ru/WCF/ClientService.svc?wsdl", params=params)
print(response.text)
#sa30716
#s4ktKFX-pN






# < ?php



#
# $client = new
# SoapClient("http://api-b2b.4tochki.ru/WCF/ClientService.svc?wsdl");
# $params = array
# (
#     'login' = > 'test',
# 'password' = > 'test',
# 'filter' = > array(
# 'season_list' = > array(0 = > 'w'),
# 'width_min' = > 185,
#                 'width_max' = > 185,
#                                 'height_min' = > 60,
#                                                  'height_max' = > 60,
#                                                                   'diameter_min' = > 15,
#                                                                                      'diameter_max' = > 15,
# ),
# 'page' = > 0,
# );
# $answer = $client->GetFindTyre($params);
# print_r($answer);
#
#? >
