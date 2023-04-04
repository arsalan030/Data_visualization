from die import Die
import plotly_express as px
# Create a D6 and a D10.
die_1 = Die(8)
die_2 = Die(8)
# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll()for _ in range(1000)]
# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)

frequencies = [results.count(value) for value in poss_results]
#Visualize the results.
title = "Results of Rolling a two 8 diec 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title,labels=labels)
# Further customize chart.
fig.update_layout(xaxis_dtick=1)
fig.show()