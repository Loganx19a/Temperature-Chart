from pathlib import Path 

import csv 

path = Path('./weather_data/sitka_weather_07-2021_simple.csv')  # build a Path object, passing it the path to the weather data file we want
lines = path.read_text().splitlines()   # read the file and chain the splitlines() method to get a list of all the lines in the file

reader = csv.reader(lines) # create a reader object using csv.reader() and pass it the list of lines from the csv file
header_row = next(reader) # gets the first line of the file, which contains the file headers
print(header_row)

''' understanding the file header data 
for index, column_header in enumerate(header_row):
    print(index, column_header)
'''

# extract the high temperatures
highs = []
# since we already read the header row, the loop will begin at the second line where the actual data begins
for row in reader: 
    high = int(row[4]) # on each pass through the loop we pull the data from index 4, corresponding to the column TMAX
    highs.append(high)

print(highs)