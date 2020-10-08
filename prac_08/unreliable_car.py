from prac_08.car import Car
import random


class Unreliable_Car(Car):
    def __init__(self, name, fuel, reliability=0.0):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if self.reliability < random.randint(0, 100):
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
