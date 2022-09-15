from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Creating an instance
die = Die()

#Make some rolls and store the result in a lst
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results) 

#Analyzing the result
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)

#Visualize the results
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)] 

x_axis_config = {'title':'Result'}
y_axis_config = {'title':'Frequency of Result'}
my_layout = Layout(title='Result of rolling one D6 100 times',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout}, filename='d6.html')
