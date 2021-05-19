class Worker:
    def __init__(self, name, surname, pos, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = pos
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):


    def get_full_name(self):
        full_name = self.name + " " + self.surname
        return full_name

    def get_total_income(self):
        total_income = sum(self._income.values())
        return total_income


pers_1 = Position("Nikol", "Bobrova", "pilot", 500, 1000)

print(pers_1.get_full_name())
print(pers_1.get_total_income())
