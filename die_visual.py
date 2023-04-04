from die import Die
import plotly_express as px

die = Die()
"Make some roll store result in a list"
results = [die.roll()for _ in range(1000)]

print(results)

# Analyze the results.
poss_results = range(1, die.num_sides + 1)

frequencies = [results.count(value) for value in poss_results]
# Visualize the results.
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title,labels=labels)
fig.show()
print(frequencies)
