class Cell:


    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __str__(self):
        return f"The cell number is {self.number}"

    def __sub__(self, other):
       return Cell(self.number - other.number) if self.number - other.number > 0 else print("Negative result")

    def __str__(self):
        return f"The cell number is {self.number}"

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __str__(self):
        return f"The cell number is {self.number}"

    def __truediv__(self, other):
       return Cell(self.number / other.number)

    def __str__(self):
        return f"The cell number is {self.number}"

cell1 = Cell(6)
cell2 = Cell(8)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)