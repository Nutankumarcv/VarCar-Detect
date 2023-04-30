import configparser

config = configparser.ConfigParser()
config.read('/Users/newowner/Documents/Clients/Varcar-2/src/config.ini')
realWorldLength = float(config['calibrations']['real_world_lenght']) # Meters
pixelLength = float(config['calibrations']['pixels_length']) # Pixels

convertationFactor = realWorldLength / pixelLength


def kilometer_per_hour(speed_pixels_per_second):
    speed_meters_per_second = speed_pixels_per_second * convertationFactor
    return speed_meters_per_second * 3.6

def miles_per_hour(speed_pixels_per_second):
    speed_meters_per_second = speed_pixels_per_second * convertationFactor
    return speed_meters_per_second * 2.237
