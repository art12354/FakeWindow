from SunData import SunData
def convertTimeToIntensity(time):

    civilTwilightBeginINTENSITY = 0
    sunriseINTENSITY = 30
    solarNoonINTENSITY = 80
    sunsetINTENSITY = 20
    civilTwilightEndINTENSITY = 0
    
    currentTime = time
    data = SunData()
    civilTwilightBegin = data.getCivilTwilightBegin()
    sunrise = data.getSunrise()
    solarNoon = data.getSolarNoon()
    sunset = data.getSunset()
    civilTwilightEnd = data.getCivilTwilightEnd()

    timeCutOffs = [civilTwilightBegin, sunrise, solarNoon, sunset, civilTwilightEnd]
    intensities = [civilTwilightBeginINTENSITY, sunriseINTENSITY, solarNoonINTENSITY, sunsetINTENSITY, civilTwilightEndINTENSITY]

    #print('DEBUG: ', '\n', 'currentTime: ', currentTime, '\n', 'timeCutOffs: ', timeCutOffs, '\n', 'intensities: ', intensities, '\n')

    if(currentTime < timeCutOffs[0]):
        return intensities[0]

    if(currentTime > timeCutOffs[len(timeCutOffs)-1]):
        return intensities[len(intensities)-1]

    for i in range(len(timeCutOffs)):
        #print('DEBUG: ', 'iteration: ', i, '\n')
        if(i == 0):
            continue
        if(i == len(timeCutOffs)):
            break
        rangeStartTime = timeCutOffs[i]
        rangeEndTime = timeCutOffs[i+1]
        #print('DEBUG: ', '\n', 'rangeStartTime: ', rangeStartTime, '\n', 'rangeEndTime: ', rangeEndTime, '\n', 'currentTime: ', currentTime, '\n')
        if(rangeEndTime < currentTime):
            continue
        percent = (currentTime - rangeStartTime) / (rangeEndTime - rangeStartTime)
        #print('DEBUG: ', percent, '\n')
        return lerp(intensities[i], intensities[i+1], percent)

def lerp(a, b, c):
    return a + ((b-a)*c)
