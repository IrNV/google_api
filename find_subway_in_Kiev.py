import googlemaps

api_key = "key"
gmaps = googlemaps.Client(key=api_key)

location = (50.5017166, 30.497994)  # Координаты в радиусе которых мы ищем метро
radius = 5000  # радиус
place = gmaps.places('subway_station', location=location,
                     radius=radius, type="subway_station")

results = place["results"]
for result in results:
    print("Название: метро", result["name"], result["geometry"]["location"])
    print("\n")


