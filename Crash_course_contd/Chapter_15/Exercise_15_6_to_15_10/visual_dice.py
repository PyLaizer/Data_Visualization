#Exercise 15.6 & 15.9

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Creating the die instance for an 8-sided die
die_1 = Die(8)
die_2 = Die(8)

results = [die_1.roll() + die_2.roll() for num in range(1000)]
# for num in range(10000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# print(results)  
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for num in range(2, max_result+1):
    frequency = results.count(num)
    frequencies.append(frequency)

# print(frequencies)

x_values = list(range(2,max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result','dtick':1}
y_axis_config = {'title':'Frequencies'}
layout = Layout(title='Rolling two D8 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':layout}, filename='d8_d8.html')