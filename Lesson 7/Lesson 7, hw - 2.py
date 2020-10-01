from abc import ABC, abstractmethod


class Wear(ABC):
    @abstractmethod
    def material(self):
        pass

    def __init__(self, v=55, h=1.75):
        self.v = v
        self.h = h

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 42:
            self.__v = 42
        elif v > 66:
            self.__v = 66
        else:
            self.__v = v

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h > 2.3:
            self.__h = 2.3
        elif h < 1.2:
            self.__h = 1.2
        else:
            self.__h = h


class coat(Wear):
    @property
    def material(self):
        return round(self.v / 6.5 + 0.5, 2)


class suit(Wear):
    @property
    def material(self):
        return round(2 * self.h + 0.3, 2)


v = 56
h = 1.8

a = coat(v, h)
print(f'\nРазмер одежды - {v} (размеры от 42 до 66)\nИспользовано материала для пальто: {a.material} м')

b = suit(v, h)
print(f'\nРост - {h} (рост от 1.3 до 2.3)\nИспользовано материала для костюма: {b.material} м\n')

print('Общий расход ткани на пальто и костюм:')
print(f'{round(a.material + b.material, 2)} м')
