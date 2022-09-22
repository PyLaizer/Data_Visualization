#Exercise 16.3

import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/san_francisco_2018.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #generating data
    san_fran_dates = []
    san_fran_highs = []
    san_fran_lows = []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high_temp = int(row[4])
            low_temp = int(row[5]) 
        except ValueError:
            print(f"Missing data for the date: {current_date}") 
        else:
            san_fran_dates.append(current_date)
            san_fran_highs.append(high_temp)
            san_fran_lows.append(low_temp)    

#Plotting the data in a temperature chart
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(san_fran_dates,san_fran_highs, c='red')
ax.plot(san_fran_dates,san_fran_lows, c='blue')    

#Format the plot
ax.set_title("High and low temparatures for San Francisco \n 2018", fontsize=20)
ax.set_xlabel('Dates',fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (Highs and lows)", fontsize=10)
ax.set_ylim(0,100)
ax.tick_params(axis='both', which='major', labelsize=10)

plt.show()
        