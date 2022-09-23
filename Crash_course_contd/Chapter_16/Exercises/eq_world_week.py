#Exercise 16.8

import json

from plotly.graph_objs import Layout
from plotly import offline

#Explore the structure of the data
filename = 'data/JSON_data/all_eq_4_5_week.json'
with open(filename, encoding='cp437') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
all_eq_title = all_eq_data['metadata']['title']

mags = []
lons = []
lats = []
all_text_info = []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    text_info = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    all_text_info.append(text_info)

#MAP the earthquake
data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':all_text_info,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale':'YlGnBu',
        'reversescale':False,
        'colorbar':{'title':'magnitude'},
    },
}]

my_layout = Layout(title=all_eq_title)

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes_week.html')
