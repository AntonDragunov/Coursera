from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

# map_data = list(map(lambda num: round(num ** 2, 1), data))
filter_data = list(
    filter(lambda item: int(item[1]) if int(item[1]) > 10000000 and item[2] == 'primary' else None, data))
map_data = list(map(lambda item: item[0], filter_data))
sort_data = list(sorted(map_data, key=lambda item: item))
# reduce_result = reduce(lambda num1, num2: num1 * num2, data, 1)
# print(filter_data)
#print(sort_data)
# print('Cities:', end='')
# print(reduce(lambda item, x:  item +', ' , sort_data, ' '))
# reduce(lambda x, y: f'{x} {y},', sort_data, 'Cities:').strip(',')
print("Cities:", reduce(lambda x, y: x + ', ' + y, sort_data))
# print(new_data)
# Cities: Beijing, Buenos Aires, ...
