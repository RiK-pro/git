from time import sleep
from colorama import Fore


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        while True:
            print(Fore.RED, TrafficLight.__color[0])
            sleep(7)
            print(Fore.YELLOW, TrafficLight.__color[1])
            sleep(2)
            print(Fore.GREEN, TrafficLight.__color[2])
            sleep(7)
            print(Fore.YELLOW, TrafficLight.__color[1])
            sleep(2)


lighton = TrafficLight()
lighton.running()
