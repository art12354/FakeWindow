from SunData import SunData
#from ledDriver import ledDriver
from datetime import datetime
from time import sleep
from threading import Thread
from convertTimeToIntensity import convertTimeToIntensity
import pytz

data = SunData()

def refreshSunData():
    data.refreshSunData()
    print("refreshed sun data")

def window():
    print("starting Window")
    while(True):
        #send system time to function and gather intensity
        intensity = convertTimeToIntensity(pytz.utc.localize(datetime.utcnow()).astimezone(pytz.timezone('US/Central')))
        #send intensity to driver
        #ledDriver(intensity)
        print('Window intensity: ', intensity, '\n')
        sleep(60)

windowThread = Thread(target=window)
    
windowThread.start()

while(True):
    sleep(86400)
    refreshSunData()

