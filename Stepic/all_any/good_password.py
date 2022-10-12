# n = str(input())
#
#
# for i in n:
#     if len(n) >= 7:
#         result = any(lambda x: x.isdigit()) or x.islower() or x.ishigher(), n)
#         p
#
#
#     else:
#         print('NO')
#
#
#
s=input()
print(('NO', 'YES')[len(s)>=7 and s.upper()!=s and s.lower()!=s and any(map(lambda x: True if x in '0123456789' else False,s))])