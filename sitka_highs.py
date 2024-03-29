from pathlib import Path 

import csv 
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('./weather_data/sitka_weather_2021_simple.csv')  # build a Path object, passing it the path to the weather data file we want
lines = path.read_text().splitlines()   # read the file and chain the splitlines() method to get a list of all the lines in the file

reader = csv.reader(lines) # create a reader object using csv.reader() and pass it the list of lines from the csv file
header_row = next(reader) # gets the first line of the file, which contains the file headers

# extract the dates and high/low temperatures
dates, highs, lows = [], [], []
# since we already read the header row, the loop will begin at the second line where the actual data begins
for row in reader: 
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4]) # on each pass through the loop we pull the data from index 4, corresponding to the column TMAX
    low = int(row[5]) # TMIN
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# plot the high and low temperatures
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, highs, color='firebrick', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# formal plot
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()