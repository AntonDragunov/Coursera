is_non_negative_num = lambda x: True if (x.replace('.', '', 1)).isdigit() and int((x.replace('.', '', 1))) >= 0 else False
#print(str('10.45'.replace('.', '', 1))).isdigit()
# print(is_non_negative_num('121245'))
print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))

# неотрицательным числом (целым или вещественным)
