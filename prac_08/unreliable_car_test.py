from prac_08.unreliable_car import Unreliable_Car


def main():
    my_car = Unreliable_Car("Prius 1", 100, 50.0)
    my_car.drive(40)
    print("my car is a {} it has {} fuel and has driven {}".format(my_car.name, my_car.fuel, my_car.odometer))


main()
