import googlemaps
import csv


class GoogleAPI:
    def __init__(self):
        # считываемданные о местоположении метро с файла
        self.subways = GoogleAPI.get_data_from_file()
        self.gmaps = googlemaps.Client(key='your API key')

    @classmethod
    def get_data_from_file(cls):
        subways = []
        """
        csv файл представляет собой такую структуру:
        Название метро,широта,долгота
        Арсенальна,50.4444465,30.5454041
        ...
        """
        with open("subways.csv", "r") as data_file:
            reader = list(csv.reader(data_file))

            rows = reader[1:]

            for row in rows:
                subways.append((row[1], row[2]))

        return subways

    def get_min_len_subways(self, origin):
        origins = [origin]

        # находим минимальную дистанцию
        matrix = self.gmaps.distance_matrix(origins, self.subways, mode="driving")

        if matrix["status"] != "OK":
            return "Google api cant use this name of house"

        # результат приходит в формате json, поэтому дастаем растояния к метро из json результата
        result = []
        for distance in matrix["rows"][0]["elements"]:
            result.append(float(distance["distance"]["text"].replace(" km", "").replace(",", ".")))

        return min(result)


g_api = GoogleAPI()
data = "бульвар Леонида Быкова, 5"
print(g_api.get_min_len_subways(data))
