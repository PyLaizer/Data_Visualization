#Exercise 16.4

import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Getting the index of the required headers
    for index, column_header in enumerate(header_row):
        if column_header == "DATE":
            date_index = index
        if column_header == "TMAX":
            tmax_index = index
        if column_header == "TMIN":
            tmin_index = index
        if column_header == "NAME":
            name_index = index  

    #Extracting and reading data
    highs = []
    lows = []
    dates = []

    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[tmax_index])
            low = int(row[tmin_index])
            station_name = row[name_index]
        except ValueError:
            print(f"Missing data for the date: {current_date}")    
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#Plotting Data in a Temperature Chart
#Plot the high and low temperatures
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates, highs,c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)

# #Shading an area in the chart
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# #Format Plot
plt.title(f"Daily high and low temperatures for {station_name} - 2018", fontsize=18)
plt.xlabel('Dates',fontsize=10)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=8)

plt.show()
