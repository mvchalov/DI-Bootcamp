import datetime

import air
import random
import string


class AirTest:
    def __init__(self):
        self.airports = []
        self.init_airports()
        self.airlines = []
        self.init_airlines()
        self.init_planes()
        self.test_it()

    def init_airports(self):
        cities = [
            'Tel Aviv',
            'Tokyo',
            'Stockholm',
            'Seoul',
            'Paris',
            'Munich',
            'Zurich',
            'Madrid'
        ]
        for _ in range(random.randint(2, 4)):
            while True:
                temporary_city = cities[random.randint(0, len(cities) - 1)]
                if len(list(filter(lambda e: e.city == temporary_city, self.airports))) == 0:
                    break
            self.airports.append(air.Airport(temporary_city))

    def init_airlines(self):
        for _ in range(random.randint(1, 10)):
            while True:
                temporary_id = [*string.ascii_uppercase]
                random.shuffle(temporary_id)
                temporary_id = ''.join(random.choices(temporary_id, k=2))
                if len(list(filter(lambda e: e.id == temporary_id, self.airlines))) == 0:
                    break
            while True:
                temporary_name = [*string.ascii_lowercase]
                random.shuffle(temporary_name)
                temporary_name = ''.join(random.choices(temporary_name, k=random.randint(2, 10)))
                if len(list(filter(lambda e: e.name == temporary_name, self.airlines))) == 0:
                    break
            temporary_name = temporary_name[0].upper() + temporary_name[1:]
            self.airlines.append(air.Airline(temporary_id, temporary_name))

    def init_planes(self):
        for i in range(random.randint(10, 99)):
            airport = self.airports[random.randint(0, len(self.airports)-1)]
            company = self.airlines[random.randint(0, len(self.airlines)-1)]
            plane = air.Airplane(i + 1, airport, company)
            airport.planes.append(plane)
            company.planes.append(plane)

    def show_airports(self):
        for e in self.airports:
            print(f"The airport of {e.city} has {len(e.planes)} planes now")

    def show_airlines(self):
        for e in self.airlines:
            print(f"{e.name} ({e.id}) has {len(e.planes)} planes")

    def show_planes_info(self):
        print("We have these airlines:")
        line_order = {}
        for i, e in enumerate(self.airlines):
            print(str(i)+': '+e.name)
            line_order[e.name]: i
        choice = int(input("Choose the airline: "))
        if self.airlines[choice]:
            for e in self.airlines[choice].planes:
                print(f"Plane {e.id} belongs to {e.company.name} and located in {e.current_location.city} now")

    def schedule_random_flight(self):
        flight_date = datetime.date(random.randint(datetime.date.today().year, datetime.date.today().year+2),
                                    random.randint(1, 12), random.randint(1, 31))
        airport = self.airports[random.randint(0, len(self.airports)-1)]
        while True:
            destination = self.airports[random.randint(0, len(self.airports)-1)]
            if destination != airport:
                break
        company = self.airlines[random.randint(0, len(self.airlines)-1)]
        if airport.schedule_flight(destination, flight_date, company):
            print("The flight is scheduled")
        else:
            print("There's no plane available")

    def show_info(self):
        for a in self.airports:
            a.info(datetime.date.today(), datetime.date.today() + datetime.timedelta(days=365))


    def test_it(self):
        while True:
            print("MENU:")
            print("—" * 30)
            print("1: Show the airports")
            print("2: Show the airlines")
            print("3: Show planes of a company")
            print("4: Schedule a random flight")
            print("5: Show info")
            print("q: Quit")
            print("—" * 30)
            choice = input("Enter your choice: ")
            if choice == '1':
                self.show_airports()
            elif choice == '2':
                self.show_airlines()
            elif choice == '3':
                self.show_planes_info()
            elif choice == '4':
                self.schedule_random_flight()
            elif choice == '5':
                self.show_info()
            elif choice.lower() == 'q':
                break


test = AirTest()
