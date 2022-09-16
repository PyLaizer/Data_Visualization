#Exercise 15.10

import plotly.express as px
from random_walk import RandomWalk

#Creating random walk instance
rw = RandomWalk()
rw.fill_walk()

fig = px.scatter(x=rw.x_values,y=rw.y_values)
fig.show()