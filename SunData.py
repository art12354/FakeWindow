from datetime import datetime
import urllib3
import sys
import json
from pytz import timezone
class SunData:

    def __init__(self):
        self.http = urllib3.PoolManager()
        self.response = self.http.request('Get', 'https://api.sunrise-sunset.org/json?lat=43.073051&lng=-89.401230&formatted=0')
        self.parsedContents = json.loads(self.response.data)
        self.civilTwilightBegin = datetime.strptime(self.parsedContents["results"]["civil_twilight_begin"], "%Y-%m-%dT%H:%M:%S%z").astimezone(timezone('US/Central'))
        self.sunrise = datetime.strptime(self.parsedContents["results"]["sunrise"], "%Y-%m-%dT%H:%M:%S%z").astimezone(timezone('US/Central'))
        self.solarNoon = datetime.strptime(self.parsedContents["results"]["solar_noon"], "%Y-%m-%dT%H:%M:%S%z").astimezone(timezone('US/Central'))
        self.sunset = datetime.strptime(self.parsedContents["results"]["sunset"], "%Y-%m-%dT%H:%M:%S%z").astimezone(timezone('US/Central'))
        self.civilTwilightEnd = datetime.strptime(self.parsedContents["results"]["civil_twilight_end"], "%Y-%m-%dT%H:%M:%S%z").astimezone(timezone('US/Central'))
            
    def refreshSunData(self):
        self.http = urllib3.PoolManager()
        self.response = self.http.request('Get', 'https://api.sunrise-sunset.org/json?lat=43.073051&lng=-89.401230&formatted=0')
        self.parsedContents = json.loads(self.response.data)
        self.civilTwilightBegin = datetime.strptime(self.parsedContents["results"]["civil_twilight_begin"], "%Y-%m-%dT%H:%M:%S%z").astimezone(timezone('US/Central'))
        self.sunrise = datetime.strptime(self.parsedContents["results"]["sunrise"], "%Y-%m-%dT%H:%M:%S%z").astimezone(timezone('US/Central'))
        self.solarNoon = datetime.strptime(self.parsedContents["results"]["solar_noon"], "%Y-%m-%dT%H:%M:%S%z").astimezone(timezone('US/Central'))
        self.sunset = datetime.strptime(self.parsedContents["results"]["sunset"], "%Y-%m-%dT%H:%M:%S%z").astimezone(timezone('US/Central'))
        self.civilTwilightEnd = datetime.strptime(self.parsedContents["results"]["civil_twilight_end"], "%Y-%m-%dT%H:%M:%S%z").astimezone(timezone('US/Central'))
            
    def getCivilTwilightBegin(self):
        return self.civilTwilightBegin

    def getSunrise(self):
        return self.sunrise

    def getSolarNoon(self):
        return self.solarNoon

    def getSunset(self):
        return self.sunset

    def getCivilTwilightEnd(self):
        return self.civilTwilightEnd

    def printData(self):
        print('Civil Twilight Begin: ', self.civilTwilightBegin, '\n', 'Sunrise: ', self.sunrise, '\n', 'Solar Noon: ', self.solarNoon, '\n', 'Sunset: ', self.sunset, '\n', 'Civil Twilight End: ', self.civilTwilightEnd, '\n')
