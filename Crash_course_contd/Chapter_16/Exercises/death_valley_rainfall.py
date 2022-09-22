# Exercise 16.1 : Death Valley Rainfall
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index,c_header in enumerate(header_row):
    #     print(c_header)

    #Generating data
    dates = []
    prcps = []
    for row in reader:
        current_date =  datetime.strptime(row[2], '%Y-%m-%d')   
        current_prcp = float(row[3])  
        dates.append(current_date)
        prcps.append(current_prcp)

#Plotting the rainfall chart
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,prcps, c='red', alpha=0.5)

#Format plot
ax.set_title('Daily rainfall in Death Valley, CA \n 2018', fontsize=20)
ax.set_xlabel('Dates',fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('Precipitation', fontsize=10)
ax.tick_params(axis='both', which='major', labelsize=10)

plt.show()
# plt.savefig('death_valley_rainfall.png',bbox_inches ='tight')         