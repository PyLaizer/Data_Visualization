#Exercise 15.7

from cgitb import html
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for num in range(3, max_result+1):
    frequency = results.count(num)
    frequencies.append(frequency)    

# print(frequencies)    

x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result','dtick':1}
y_axis_config = {'title':'Frequency'}
layout = Layout(title='Rolling three D6s 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':layout}, filename='d6_d6_d6.html')