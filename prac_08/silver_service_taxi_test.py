from prac_08.silverservicetaxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi("Prius 1", 100, 2)
    my_taxi.drive(18)
    print("my taxi is a {} it has {} fuel and my fare is {}".format(my_taxi.name, my_taxi.fuel, my_taxi.get_fare()))



main()