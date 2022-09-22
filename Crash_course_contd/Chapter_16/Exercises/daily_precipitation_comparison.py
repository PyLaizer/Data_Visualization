#Exercise 16.5

import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/Practice/phoenix_2022.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index,c_header in enumerate(header_row):
        if c_header == 'NAME':
            name_index = index
        if c_header == 'DATE':
            date_index = index
        if c_header == 'PRCP':
            prcp_index = index
        if c_header == 'SNOW':
            snow_index = index

    #Extracting and reading data
    dates = []
    total_prcp = []
    total_snow = [] 

    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        station_name = row[name_index]
        try:
            prcp = float(row[prcp_index])
            snow = float(row[snow_index])
        except ValueError:
            print(f"Missing data for the date: {current_date}")
        else:
            dates.append(current_date)  
            total_prcp.append(prcp)
            total_snow.append(snow)

filename = 'data/Practice/aberdeen_2022.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index,c_header in enumerate(header_row):
        if c_header == 'NAME':
            name_index = index
        if c_header == 'DATE':
            date_index = index
        if c_header == 'PRCP':
            prcp_index = index
        if c_header == 'SNOW':
            snow_index = index

    #Extracting and reading data
    aberdeen_dates = []
    aberdeen_total_prcp = []
    aberdeen_total_snow = [] 

    for row in reader:
        a_current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        a_station_name = row[name_index]
        try:
            a_prcp = float(row[prcp_index])
            a_snow = float(row[snow_index])
        except ValueError:
            print(f"Missing data for the date: {current_date}")
        else:
            aberdeen_dates.append(a_current_date)  
            aberdeen_total_prcp.append(a_prcp)
            aberdeen_total_snow.append(a_snow)

#Plotting the precipitation and snow chart
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,total_prcp,c='blue')
ax.plot(dates,total_snow,c='blue',alpha=0.5)
ax.plot(aberdeen_dates,aberdeen_total_prcp,c='green')
ax.plot(aberdeen_dates,aberdeen_total_snow,c='blue',alpha=0.5)

#Formatting the chart
ax.set_title(f'Daily Precipitation and snow for {station_name}\n 18/03/2022 - 07/04/2022',fontsize=10)
ax.set_xlabel('Dates',fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('Precipitation & Snow',fontsize=10)
ax.tick_params(axis='both', which='major', labelsize=8)

plt.show()
                  

        
