import plotly_express as px
from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk(5000)
rw.fill_walk()


#Visualize the results.
title = "Results of Rolling a two 8 diec 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.scatter(x=rw.x_values, y=rw.y_values)
# Further customize chart.
fig.show()