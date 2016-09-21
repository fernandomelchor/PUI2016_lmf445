###Description of PUI2016 HW2
## PUI 2016 HW 2  

##General idea and walk through by Sebastian Banos, Jonathan D. Geis and Sofiya Elyukin
##Coding for this particular notebook instance Fernando Melchor

#HW_2_1

Uploaded
show_bus_locations_lmf445.py 

python show_bus_locations.py <MTA_KEY> <BUS_LINE>

       			     C:\Users\ferna\Miniconda2\python.exe C:/Users/ferna/PycharmProjects/CUSPminiconda/show_bus_locations_lmf445.py 56e81a28-4df2-4179-9262-6cdc7dd2bb36 B52
			     http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=56e81a28-4df2-4179-9262-6cdc7dd2bb36&VehicleMonitoringDetailLevel=calls&LineRef=B52
			     Bus Line :  B52
			     Number of Active Buses :  18
			     Bus  1 at latitude  40.69152 and longitude -73.987507
			     Bus  2 at latitude  40.687277 and longitude -73.941349
			     Bus  3 at latitude  40.689461 and longitude -73.922315
			     Bus  4 at latitude  40.691059 and longitude -73.920529
			     Bus  5 at latitude  40.694871 and longitude -73.990697
			     Bus  6 at latitude  40.688491 and longitude -73.979889
			     Bus  7 at latitude  40.687699 and longitude -73.956981
			     Bus  8 at latitude  40.687398 and longitude -73.95971
			     Bus  9 at latitude  40.687978 and longitude -73.935266
			     Bus  10 at latitude  40.69695 and longitude -73.914744
			     Bus  11 at latitude  40.686109 and longitude -73.971049
			     Bus  12 at latitude  40.697161 and longitude -73.914536
			     Bus  13 at latitude  40.686975 and longitude -73.943985
			     Bus  14 at latitude  40.686076 and longitude -73.973855
			     Bus  15 at latitude  40.68619 and longitude -73.974139
			     Bus  16 at latitude  40.687486 and longitude -73.93955
			     Bus  17 at latitude  40.687963 and longitude -73.935405
			     Bus  18 at latitude  40.696116 and longitude -73.989148

#HW_2_2
##General idea and walk through by Sebastian Banos, Jonathan D. Geis and Sofiya Elyukin
##Coding for this particular notebook instance Fernando Melchor except exception for missing Data for Stops, code from Sebastian Banos, Sofiya Elyukin, Jonathan D Geis 
get_bus_info_lmf445.py

output Busline.csv

      C:\Users\ferna\Miniconda2\python.exe C:/Users/ferna/PycharmProjects/CUSPminiconda/get_bus_info_lmf445.py 56e81a28-4df2-4179-9262-6cdc7dd2bb36 B52 B52.csv
      http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=56e81a28-4df2-4179-9262-6cdc7dd2bb36&VehicleMonitoringDetailLevel=calls&LineRef=B52
      B52.csv
      Bus Number   Latitude  Longitude                  Stop Name    Stop Status
      0            1  40.691520 -73.987507         FULTON ST/SMITH ST        at stop
      1            2  40.689024 -73.981244  FULTON ST/FLATBUSH AV EXT        at stop
      2            3  40.695506 -73.916163         GATES AV/WILSON AV        at stop
      3            4  40.690448 -73.984823      FULTON ST/DUFFIELD ST        at stop
      4            5  40.698129 -73.912413      PALMETTO ST/IRVING AV        at stop
      5            6  40.690439 -73.984799      FULTON ST/DUFFIELD ST        at stop
      6            7  40.694871 -73.990697     CADMAN PZ W/TILLARY ST        at stop
      7            8  40.689411 -73.922760          GATES AV/BROADWAY    approaching
      8            9  40.686562 -73.947595          GATES AV/MARCY AV    approaching
      9           10  40.691022 -73.920565       GATES AV/BUSHWICK AV    approaching
      10          11  40.688540 -73.930388      GATES AV/MALCOLM X BL    approaching
      11          12  40.685805 -73.954175        GATES AV/BEDFORD AV    approaching
      12          13  40.686683 -73.966047    GREENE AV/WASHINGTON AV    approaching
      13          14  40.687356 -73.960225       GREENE AV/CLASSON AV    approaching
      14          15  40.686243 -73.974273     FULTON ST/S ELLIOTT PL    approaching
      15          16  40.689382 -73.923018          GATES AV/RALPH AV    approaching
      16          17  40.685437 -73.957348        GATES AV/CLASSON AV  < 1 stop away
      17          18  40.686799 -73.945530          GATES AV/MARCY AV  < 1 stop away

Process finished with exit code 0

#HW_2_3
Mockup by Fernando Melchor. Peer refinement, environmental variable call

Sofiya Elyukin, Jonathan D Geis and Sebastian Bano

https://github.com/fernandomelchor/PUI2016_lmf445/blob/master/HW2_lmf445/HW2_3_lmf445.ipynb



