class Stationery:
    def __init__(self, title="Рисуем"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой фирмы {self.title}.")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашем фирмы {self.title}.")

class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером фирмы {self.title}.")

thing_1 = Stationery()
thing_1.draw()
thing_2 = Pen("Parker")
thing_2.draw()
thing_3 = Pencil("Erich Krause")
thing_3.draw()
thing_4 = Handle("Touch")
thing_4.draw()
