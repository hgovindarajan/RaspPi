
import pywapi, serial, time, argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument("zipcode", help="The zipcode of the city you want to display")
args = parser.parse_args()

#Get the weather for the provided Zip Code
print "Getting weather for zipcode " + args.zipcode + "...",
sys.stdout.flush()
yahoo = pywapi.get_weather_from_yahoo(args.zipcode, 'imperial')
weathercom = pywapi.get_weather_from_weather_com(args.zipcode)

#Parse chances of precipitation from weather.com
if weathercom['forecasts'][0].has_key('day'):
    chance_precip = weathercom['forecasts'][0]['day']['chance_precip']
else:
    chance_precip = weathercom['forecasts'][0]['night']['chance_precip']

print "Got weather for " + yahoo['location']['city'] + ", " + yahoo['location']['region'] + "!"
print "For the date of " + yahoo['forecasts'][0]['date'] + "  High of " + yahoo['forecasts'][0]['high'] + " Low of " + yahoo['forecasts'][0]['low'] + "!"
