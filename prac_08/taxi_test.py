from prac_08.taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)

    print("my taxi is a {} it has {} fuel and my fare is {}".format(my_taxi.name, my_taxi.fuel, my_taxi.get_fare()))
    my_taxi.start_fare()
    my_taxi.drive(100)
    print("my taxi is a {} it has {} fuel and my fare is {}".format(my_taxi.name, my_taxi.fuel, my_taxi.get_fare()))






main()
