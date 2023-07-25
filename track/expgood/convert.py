# Converting lat/long to cartesian
import numpy as np
import csv

def opencsv(file):
    with open(file, newline='') as csvfile:
        return [row for row in csv.DictReader(csvfile, delimiter=',')]

data = opencsv('track/points.csv')

def get_cartesian(lat,lon):
    lat= lat* np.pi / 180
    lon= lon* np.pi / 180
    R = 6371 # radius of the earth
    x = R * np.cos(lat) * np.cos(lon)
    y = R * np.cos(lat) * np.sin(lon)
    return x,y,

for i in data:
    lon = float(i['longitude'])
    lat = float(i['latitude'])
    print(get_cartesian(lon, lat))

print(get_cartesian(41.94076496048223, -85.00154950929712))