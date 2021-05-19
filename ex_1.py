# import turtle
import time


class TrafficLight:
    __color = "grey"

    def running(self):
        while True:
            TrafficLight.__color = "red"
            print(f"Light {TrafficLight.__color}")
            time.sleep(7)
            TrafficLight.__color = "yellow"
            print(f"Light {TrafficLight.__color}")
            time.sleep(2)
            TrafficLight.__color = "green"
            print(f"Light {TrafficLight.__color}")
            time.sleep(5)
            TrafficLight.__color = "yellow"
            print(f"Light {TrafficLight.__color}")
            time.sleep(2)


t = TrafficLight()
t.running()
