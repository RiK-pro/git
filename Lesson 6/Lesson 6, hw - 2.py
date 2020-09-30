class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count(self):
        return f"Масса асфальта = {(self._length * self._width * 25 * 5 / 1000)} тонн"


r = Road(5000, 20)
print(r.count())