data = list(map(str, input().split('.')))
# data2 = []
# for item in data:
#     if len(item) > 1 and item.isdigit() and item != 0:
#         data2.append(item.lstrip('0'))
#         if item == '':
#             item = 0
#         else:
#             pass
# else:
#     data2.append(item)
# print(data2)
#result = all(map(lambda x: (x.isdigit()) and int(str(x).lstrip('0')) <= 255, data))
result = all(map(lambda elem: elem.isdigit() and 0 <= int(elem)<= 255, data))

print(result)
