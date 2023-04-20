from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


class WeatherApp:
    def __init__(self, city='Tel Aviv'):
        self.city = city

    def get_weather(self):
        owm = OWM('665c3f29d30825a32bacbb7697316420')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place('London,GB')
        w = observation.weather
        print(w.temperature('celsius') )


weather_app = WeatherApp()
weather_app.get_weather()