class Road:


    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


    def road_mass(self):
        m = self._length * self._width * 25 * 5 / 1000
        print(f'{m} тонн')

Road = Road(5000, 20)
Road.road_mass()