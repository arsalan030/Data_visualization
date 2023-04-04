import csv
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_full.csv.')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

# Extract dates, and high and low temperatures.
dates,highs, lows = [], [],[]
for _ in reader:
    date=datetime.strptime(_[2], '%Y-%m-%d')
    try:
        high = int(_[6])
        low = int(_[7])
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
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
