from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="scrapper_geo")
location = geolocator.geocode("21212122121")
print(location.address)

print((location.latitude, location.longitude))
