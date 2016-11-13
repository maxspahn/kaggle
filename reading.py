import sys
import csv
sys.path.append('/home/max/kaggle/')

ifile  = open('test.csv', "rb")
reader = csv.reader(ifile)

rownum = 0
instant = []
dteday = []
season = []
yr = []
mnth = []
hr = []
holiday = []
weekday = []
workingday = []
weathersit = []
temp = []
atemp = []
hum = []
windspeed = []

table = []
table.append(instant)
table.append(dteday)
table.append(season)
table.append(yr)
table.append(mnth)
table.append(hr)
table.append(holiday)
table.append(weekday)
table.append(workingday)
table.append(weathersit)
table.append(temp)
table.append(atemp)
table.append(hum)
table.append(windspeed)

for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for col in row:
            if(colnum == 1):
                table[colnum].append(col)
            else:
                table[colnum].append(float(col))
            colnum += 1

    rownum += 1
for x in range(0,14):
    print(table[x][300])

ifile.close()
