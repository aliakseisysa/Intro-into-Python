class Worker:


    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):


    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)


    def get_full_name(self):
        return f"{self.name} {self.surname}"


    def get_total_income(self):
        return self._income

position = Position("John", "Smith", "head", 20000)
print(position.get_full_name())
print(position.get_total_income())



