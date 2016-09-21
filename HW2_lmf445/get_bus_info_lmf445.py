#Author:Fernando Melchor PUI2016 CUSP NYU
#This script ask for 3 arguments API Key for MTA, the Busline of interest and the name of the \
# csv file that will be created as output
from __future__ import print_function
import os
import numpy as np
import pandas as pd
import json
import sys
import urllib2

MTAKEY = sys.argv[1]
BusLine = sys.argv[2]
filename = sys.argv[3]

longitude = []
latitude = []
nbuses = []
stopname = []
stopstatus = []

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTAKEY\
      +"&VehicleMonitoringDetailLevel=calls&LineRef=" + BusLine

print(url)
print(filename)
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
n = (len(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0] \
             ['VehicleActivity']))

for i in xrange(n):
   nbuses.append(i+1)
   longitude.append((dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'] \
                         [0]['VehicleActivity'][i]['MonitoredVehicleJourney']["VehicleLocation"]["Longitude"]))
   latitude.append((dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'] \
                        [0]['VehicleActivity'][i]['MonitoredVehicleJourney']["VehicleLocation"]["Latitude"]))
   onwardCallsDict = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'] \
                        [0]['VehicleActivity'][i]['MonitoredVehicleJourney']["OnwardCalls"]

##Code to ignore empty Stop Information from Sebastian Bana
   if (onwardCallsDict!={}):

       stopname.append((dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i] \
                            ['MonitoredVehicleJourney']["OnwardCalls"]["OnwardCall"][0]["StopPointName"]))
       stopstatus.append((dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i] \
                              ['MonitoredVehicleJourney']["OnwardCalls"]["OnwardCall"][0]["Extensions"]['Distances'] \
                              ['PresentableDistance']))

   else:
       stopname.append('N/A')
       stopstatus.append('N/A')

columnsnames = ['Bus Number','Latitude','Longitude','Stop Name','Stop Status']
df = pd.DataFrame(columns=columnsnames)
df['Latitude'] = latitude
df['Longitude'] = longitude
df['Bus Number'] = nbuses
df['Stop Name'] = stopname
df['Stop Status'] = stopstatus

df = df.fillna('N/A')
print(df)

df.to_csv(filename,index=False)
