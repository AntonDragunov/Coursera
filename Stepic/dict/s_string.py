s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

result = {}
l = s.split()

for num in l:
    result[num] = result.get(num, 0) + 1
#print(result)
maximum = max(result.values())
#print('максимум', (max(result.values())))
word = []

for key, value in sorted(result.items(), reverse=True, key=lambda x: x[1]):
    if value == maximum:
        word.append(key)
    else:
        pass

print(min(word))
