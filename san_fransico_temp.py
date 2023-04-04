import csv
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt
path = Path('San_Francisco_weather_data.csv.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
item='TMAX'
items='TMIN'
d='DATE'

a=header_row.index(item)
b=header_row.index(items)
c=header_row.index(d)

dates,highs,lows=[],[],[]
for row in reader:
    date=datetime.strptime(row[c], '%Y-%m-%d')
    try:
        high=int(row[a])
        low=int(row[b])
    except:
        print(f"Missing data for,{date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(date)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates,highs, color='red',alpha=0.5)
ax.plot(dates,lows,color='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# Format plot.
title = "Daily High and Low Temperatures, 2021\n'San_Francisco_weather_data"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

