class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Цвет автомобиля - {color}, Марка автомобиля - {name}")

    def go(self):
        print(f"Автомобиль {self.name} поехал")

    def stop(self):
        print(f"{self.name} резко остановилась")

    def turn_right(self):
        print(f"{self.name} повернула направо")

    def turn_left(self):
        print(f"{self.name} повернула налево")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name} - {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print(f"{self.name} превышает скорость! ({self.speed} км/ч)")
        else:
            print(f"Текущая скорость автомобиля - {self.speed} км/ч")


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print(f"машина {self.name} превышает скорость ({self.speed} км/ч)")
        else:
            print(f"Текущая скорость автомобиля - {self.speed} км/ч")


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super(PoliceCar, self).__init__(name, color, speed, is_police)

class SportCar(Car):
    def show_speed(self):
        if int(self.speed) > 100:
            print(f"машина {self.name} превышает скорость, но тебе можно ;-)({self.speed} км/ч)")
        else:
            print(f"Текущая скорость автомобиля - {self.speed} км/ч. Эта малышка может и быстрее, притопи.")

car_1 = TownCar("Chevrolet", "Синий", 80)
car_1.go()
car_1.show_speed()
car_1.turn_right()
car_1.stop()
print()

car_2 = SportCar("Lamborgini", "Желтый", 90)
car_2.go()
car_2.show_speed()
car_2.turn_left()
car_2.stop()
print()

car_3 = WorkCar("Камаз", "когда-то был красным", 41)
car_3.go()
car_3.show_speed()
car_3.stop()
print()

car_4 = PoliceCar("Лада", "Серая", 70)
car_4.go()
car_4.show_speed()
car_4.turn_left()
car_4.stop()