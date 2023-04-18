from datetime import datetime
import base64

class Airline:
    def __init__(self, airline_id, name, planes=None):
        self.id = airline_id
        self.name = name
        self.planes = planes or []


class Airplane:
    def __init__(self, plane_id, current_location, company, next_flights=None):
        self.current_location = current_location
        self.company = company
        self.next_flights = next_flights or []
        self.id = plane_id

    def fly(self, destination):
        if len(list(filter(lambda e: e.destination == destination, self.next_flights))) > 0:
            self.current_location.planes.pop(self.current_location.planes.index(self))
            self.current_location = None
            self.next_flights.pop(
                self.next_flights.index(list(filter(lambda e: e.destination == destination, self.next_flights))[0]))

    def location_on_date(self, date):
        return list(filter(lambda e: e.date == date, self.next_flights))

    def available_on_date(self, date, location):
        return self.location_on_date(date) == [location]


class Flight:
    def __init__(self, date, destination, origin, plane):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = base64.b64encode((destination.city + self.plane.company.id + str(date)).encode('utf-8'))

    def take_off(self):
        self.plane.fly()

    def land(self):
        self.plane.current_location = self.destination
        self.destination.append(self.plane)


class Airport:
    def __init__(self, city, planes=None, scheduled_departures=None, scheduled_arrivals=None):
        self.city = city
        self.planes = planes or []
        self.scheduled_departures = scheduled_departures or []
        self.scheduled_arrivals = scheduled_arrivals or []

    def schedule_flight(self, destination, flight_datetime, airline):
        available_plane = None
        for plane in airline.planes:
            location = plane.current_location
            print(location.city, flight_datetime, airline.name)
            if flight_datetime != datetime.today().date():
                if len(plane.next_flights) > 0:
                    for e in sorted(plane.next_flights, key=lambda x: x.date):
                        print(e.date, e.destination.city, e.origin.city)
                        if e.date <= flight_datetime and e.destination == self and e.origin == location:
                            available_plane = plane
                            break
                        location = e.destination
                elif location == self:
                    available_plane = plane
                    break
            elif location == self:
                available_plane = plane
                break
        if available_plane:
            new_flight = Flight(flight_datetime, destination, self, available_plane)
            available_plane.next_flights.append(new_flight)
            self.scheduled_departures.append(new_flight)
            destination.scheduled_arrivals.append(new_flight)
            return True
        else:
            return False

    def info(self, start_date, end_date):
        print(f"Between {start_date} and {end_date}")
        print(f"Departures at {self.city}:")
        for i in self.scheduled_departures:
            if start_date <= i.date <= end_date:
                print(f"ID {i.id}: on {i.date} from {i.origin.city} to {i.destination.city} by {i.plane.company.name}")
        print(f"Arrivals at {self.city}:")
        for i in self.scheduled_arrivals:
            if start_date <= i.date <= end_date:
                print(f"ID {i.id}: on {i.date} from {i.origin.city} to {i.destination.city} by {i.plane.company.name}")
