""" 
dht22.py 
Temperature/Humidity monitor using Raspberry Pi and DHT22.
Also a rpi temp monitor. 
Data is displayed at thingspeak.com
Original author: Mahesh Venkitachalam at electronut.in 
Modified by Adam Garbo on December 1, 2016 
Modified by Marin Barsic on July 2, 2017
""" 
import sys 
import RPi.GPIO as GPIO 
from time import sleep 
import Adafruit_DHT 
import urllib2 
import httplib, urllib

myAPI = "YOUR THINGSPEAK API KEY HERE" 
def getSensorData(): 
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4) 
   temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 
   return (str(RH), str(T), str(temp))
def main(): 
   print 'starting...' 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 
   while True: 
       try: 
           RH, T, temp = getSensorData() 
           f = urllib2.urlopen(baseURL + 
                               "&field1=%s&field2=%s&field3=%s" % (RH, T, temp)) 
           print f.read() 
           f.close() 
           sleep(300) #uploads DHT22 sensor and cpu temp values every 5 minutes 
       except: 
           print 'exiting.' 
           break 
# call main 
if __name__ == '__main__': 
   main()  
