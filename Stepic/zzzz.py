myset = set()
for i in range(10):
    if i % 2 == 0:
        myset.add('even')
    else:
        myset.add('odd')
print(len(myset))
