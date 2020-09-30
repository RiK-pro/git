class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"Месячный заработок {sum(self._income.values())} рублей"


worker_1 = Position("Петя", "Простоватов", "работяга", 20000, 5000)
print(worker_1.get_full_name())
print(f"должность: {worker_1.position}")
print(worker_1.get_total_income())
print()
worker_2 = Position("Александр", "Клюев", "сверхчеловек", 400000, 120000)
print(worker_2.get_full_name())
print(f"должность: {worker_2.position}")
print(worker_2.get_total_income())