from random import choice


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} started")

    def stop(self):
        print(f"{self.name} stopped")

    def turn(self):
        direction = ["forward", "backward", "right", "left"]
        print(f"{self.name} moves {choice(direction)}")

    def show_speed(self):
        print(f"{self.name} speed {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Attention! Speed {self.name} speed higher than allowed!")
        else:
            print(f"{self.name} speed {self.speed} OK")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Attention! Speed {self.name} higher than allowed!")
        else:
            print(f"{self.name} speed {self.speed} normal")


class PoliceCar(Car):
    pass


auto_1 = WorkCar(30, "orange", "KAMAZ")
print(f"Go to the start {auto_1.color} {auto_1.name} is WorkCar")
auto_1.go()
auto_1.turn()
auto_1.show_speed()
auto_1.stop()
auto_2 = SportCar(150, "red", "Ferrari")
print(f"Go to the start {auto_2.color} {auto_2.name} is SportCar")
auto_2.go()
auto_2.turn()
auto_2.show_speed()
auto_2.stop()
auto_3 = TownCar(80, "green", "Toyota")
print(f"Go to the start {auto_3.color} {auto_3.name} is TownCar")
auto_3.go()
auto_3.turn()
auto_3.show_speed()
auto_3.stop()
auto_4 = PoliceCar(80, "green", "Ford", True)
print(f"Go to the start {auto_4.color} {auto_4.name} is PoliceCar")
auto_4.go()
auto_4.turn()
auto_4.show_speed()
auto_4.stop()
