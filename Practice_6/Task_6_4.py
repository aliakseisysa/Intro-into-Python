class Car:


    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        print("The car has moved")

    def stop(self):
        print("The car has stopped")

    def turn(self, direction):
        self.direction = direction
        print(f"The car has turned {direction}")

    def show_speed(self):
        print(f"Your current speed is {self.speed} km/h")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Your current speed is overlimit")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Your current speed is overlimit")


car = Car(50, "white", "Ford", True)
car.go()
car.stop()
car.turn("left")
car.show_speed()
town_car = TownCar(90, "white", "Ford", False)
town_car.go()
town_car.stop()
town_car.turn("right")
town_car.show_speed()