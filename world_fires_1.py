import csv
from pathlib import Path
from plotly.graph_objs import Scattergeo, Layout
from datetime import datetime
from plotly import offline


path = Path('eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

# Extract dates, and high and low temperatures.
dates,lats, lons , brightnesses,hover_texts = [], [],[],[], []
for _ in reader:
    date=datetime.strptime(_[5], '%Y-%m-%d')
    brightness = float(_[2])
    label = f"{date.strftime('%m/%d/%y')} - {brightness}"
    try:
        lat = (_[0])
        lon = (_[1])
    except:
        print(f"Missing data for,{date}")
    else:
        lats.append(lat)
        lons.append(lon)
        brightnesses.append(brightness)
        dates.append(date)

# Map the fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [brightness/20 for brightness in brightnesses],
        'color': brightnesses,
        'colorscale': 'YlOrRd',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title='Global Fire Activity')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')




