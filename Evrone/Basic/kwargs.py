def init_settings(**init):
    result = {}
    for key, value in init.items():
        result[key.upper()] = value
    return result

print(init_settings(foo=1, bar=2, peso=3))

