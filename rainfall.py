import datetime

cities = {}


class CityRainfall:
    __global_reports = {}

    def __init__(self, name: str):
        self.__name = name
        self.__rain_reports = {}

    def add_rain(self, rain_mm: int):
        update = {datetime.datetime.now(): rain_mm}
        self.__rain_reports.update(update)
        self.__global_reports.update(update)

    def __average(self) -> float:
        t = self.__total()
        c = len(self.__rain_reports.keys())
        return self.__calculate_average(t, c)

    def __total(self) -> int:
        return sum(self.__rain_reports.values())

    def __global_average(self) -> float:
        t = sum(self.__global_reports.values())
        c = len(self.__global_reports.keys())
        return self.__calculate_average(t, c)

    @staticmethod
    def __calculate_average(t: int, c: int) -> float:
        if not c:
            return 0

        return t / c

    def __str__(self) -> str:
        return f'{self.__name}: total mm of rain {self.__total()}, average report: {self.__average()}, overall average: {self.__global_average()}'


while True:
    city_input = input('city: ')
    if not city_input:
        break

    rain_input = input('rain in mm: ')
    if not rain_input.isdigit():
        print(f'{rain_input} is not numerical')
        break

    if city_input not in cities.keys():
        cities.update({city_input: CityRainfall(city_input)})

    cities.get(city_input).add_rain(int(rain_input))

for city in cities.values():
    print(city)
