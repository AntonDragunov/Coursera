a = str(input())
price = len(a) * 60

price_rub = price // 100
price_kop = price % 100

print(price_rub, "р. ", price_kop, "коп.")
