pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}

for info in pets:
    result[info[1:]] = result.get(info, [])

print(result)

for info in pets:
    result[info] = info.setdefault

# for dog in result:
#     if dog not in result:
#         result[dog] == value
#     else:
#         result[dog] += value

# for value in sorted(result.items(), key=lambda x: x[0]):
#     print(value)
#     result.values() += value

print(result)