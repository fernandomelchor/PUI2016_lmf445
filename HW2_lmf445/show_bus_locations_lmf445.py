#Author:Fernando Melchor PUI2016 CUSP NYU
#This script ask for 2 arguments API Key for MTA, the Busline of interest it returns a list of buses \
# in the Bus Line of interest and the Latitude and Logitude of them.
from __future__ import print_function
import os
import json
import sys
import urllib2

MTAKEY = sys.argv[1]
BusLine = sys.argv[2]

longitude = []
latitude = []
nbuses = []
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTAKEY \
      +"&VehicleMonitoringDetailLevel=calls&LineRef=" + BusLine

print(url)
##From Prof. Federica Bianco Example NYUweatherAPI.py
response = urllib2.urlopen(url)
data = response.read().decode('utf-8')
dataDict = json.loads(data)

##TESTING OFFLINE
#location="responseB52.json"
#print(location)
#jsonfile = open(location,'r')
#dataDict = json.load(jsonfile)
#print(dataDict['Siri']['ServiceDelivery'].keys())
#print(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
n = (len(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']))

for i in xrange(n):
   nbuses.append(i+1)
   longitude.append((dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'] \
                         [i]['MonitoredVehicleJourney']["VehicleLocation"]["Longitude"]))
   latitude.append((dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'] \
                        [i]['MonitoredVehicleJourney']["VehicleLocation"]["Latitude"]))

print('Bus Line : ',BusLine)
print('Number of Active Buses : ',n)
for i in xrange(n):
      print('Bus ',nbuses[i],'at latitude ',latitude[i],'and longitude',longitude[i])