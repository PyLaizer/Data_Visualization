#Exercise 16.2

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Extracting and reading data
    highs_sitka = []
    lows_sitka = []
    dates_sitka = []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:        
            dates_sitka.append(current_date)
            highs_sitka.append(high)
            lows_sitka.append(low)

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Extracting and reading data
    highs_death = []
    lows_death = []
    dates_death = []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:        
            dates_death.append(current_date)
            highs_death.append(high)
            lows_death.append(low)            


# Plotting Data in a Temperature Chart
# Plot the high and low temperatures
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates_sitka, highs_sitka,c='blue')
ax.plot(dates_sitka, lows_sitka,c='blue', alpha=0.5)
ax.plot(dates_death, highs_death, c='red')
ax.plot(dates_death, lows_death, c='red', alpha=0.5)

#Shading an area in the chart
plt.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)
plt.fill_between(dates_death, highs_death, lows_death, facecolor='red', alpha=0.1)

#Format Plot
plt.title("Daily high and low temperatures - 2018\n Death Valley, CA & Sitka, Alaska", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
# plt.savefig('Daily_comparison_of_temperatues_between_death_valley_and_sitka.png',bbox_inches='tight')

    