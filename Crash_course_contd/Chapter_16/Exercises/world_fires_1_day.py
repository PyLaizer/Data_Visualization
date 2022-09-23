#Exercise 16.9

import csv

from plotly.graph_objs import Layout
from plotly import offline
from datetime import datetime

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index,c_header in enumerate(header_row):
        if c_header == 'latitude':
            lat_index = index
        if c_header == 'longitude':
            lon_index = index
        if c_header == 'brightness':
            brightness_index  = index
        if c_header == 'acq_date':
            date_index = index
        if c_header == 'acq_time':
            time_index = index        

    lats = []
    lons = []
    total_brightness = []
    total_date = []
    total_time = []

    for row in reader:
        try:
            lat = float(row[lat_index])
            lon = float(row[lon_index])
            brightness = float(row[brightness_index])
            current_date = datetime.strptime(row[date_index],'%Y-%m-%d')
        except ValueError:
            print(f"Missing data / corrupted data")
        else:
            lats.append(lat)
            lons.append(lon)
            total_brightness.append(brightness)
            total_date.append(current_date)  

#Mapping the world fires
data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':total_date,
    # 'marker':{
    #     'size':[brightness / 10 for brightness in total_brightness],
    #     'color':total_brightness,
    #     'colorscale':'Viridis',
    #     'reversescale':True,
    #     'colorbar':{'title':'Brightness of Fire'}
    # }
}]   

my_layout = Layout(title='World fires\n 22-09-2018 to 23-09-2018')

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename="world_fires_09_22_2018.html")
         
