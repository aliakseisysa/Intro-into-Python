class Textil:
    def __init__(self, V, H):
        self.V = V
        self.H = H

    def get_expend_c(self):
        return self.V / 6.5 + 0.5

    def get_expend_j(self):
        return self.H * 2 + 0.3

    @property
    def get_expend_full(self):
        return str(f'Расход ткани \n'
                   f' {(self.V / 6.5 + 0.5) + (self.H * 2 + 0.3)}')


class Coat(Textil):
    def __init__(self, V, H = 0):
        super().__init__(V, H)
        self.expend_c = self.V / 6.5 + 0.5

    def __str__(self):
        return f'Расход ткани на пальто {self.expend_c}'


class Jacket(Textil):
    def __init__(self, H, V = 0):
        super().__init__(V, H)
        self.expend_j = self.H * 2 + 0.3

    def __str__(self):
        return f'Расход ткани на костюм {self.expend_j}'

coat = Coat(38)
jacket = Jacket(1.75)
textil = Textil(38, 1.75)
print(coat)
print(jacket)
print(textil.get_expend_full)
print(coat.get_expend_c())
print(jacket.get_expend_j())