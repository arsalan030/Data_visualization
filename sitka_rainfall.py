import csv
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

dates, rain_falls, = [], []
for row in reader:
    rain_fall = float(row[5])
    date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(date)
    rain_falls.append(rain_fall)

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,rain_falls,color='blue')
title = "Daily Rain fall amount, 2021\nsitka_weather_2021"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (R)", fontsize=16)
ax.tick_params(labelsize=16)

first_date = datetime.strptime('2021-07-01', '%Y-%m-%d')
plt.show()
