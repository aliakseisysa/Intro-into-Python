class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки ручкой")


class Penсil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки карандашем")


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки маркером")

pen = Pen("pen")
pen.draw()

pencil = Penсil("pencil")
pencil.draw()

handle = Handle("handle")
handle.draw()
