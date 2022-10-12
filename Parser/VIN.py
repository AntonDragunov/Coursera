from vininfo import Vin

vin = Vin('XW8LC6NU3MH200398')

print(vin.country, vin.manufacturer, vin.region, vin.years, vin.details)  # France vin.details.model.code, vin.details.model.name,
vin.manufacturer  # Renault
vin.region  # Europe
vin.wmi  # VF1
vin.vds  # LM1B0H
vin.vis  # 36666155

annotated = vin.annotate()
details = vin.details

vin.verify_checksum()  # False
Vin('1M8GDM9AXKP042788').verify_checksum()  # True
