class Scoop:
    def __init__(self, flavor: str):
        self.__flavor = flavor

    def __str__(self) -> str:
        return self.__flavor


class Bowl:
    def __init__(self):
        self.__scoops = []

    def add_scoops(self, *scoops: Scoop) -> None:
        for scoop in scoops:
            self.__scoops.append(scoop)

    def __repr__(self) -> str:
        return '\n'.join(str(scoop) for scoop in self.__scoops)


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b)
