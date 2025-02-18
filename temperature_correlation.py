import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Data
filename1 = 'stations.json.gz'
filename2 = 'city_data.csv'

stations = pd.read_json(filename1, lines=True)
datac = pd.read_csv(filename2)


def clean_city_data(datac):
    datac.loc[:, 'area'] = datac['area'] / 1000000 
    datac = datac.dropna()
    datac = datac[datac['area'] < 10000]  
    datac= calden(datac) 
    return datac


def calden(datac):

    datac.loc[:, 'density'] = datac['population'] / datac['area']
    return datac


datac = clean_city_data(datac)


def convertcel(stations):
    
    stations.loc[:, 'avg_tmax'] = stations['avg_tmax'] / 10.0
    return stations


stations = convertcel(stations)


def distance(city, stations):
    lat2, lon2 = city['latitude'], city['longitude']

    pi_radians = np.pi

    converts = pi_radians / 180.0

    latd = (lat2 - stations['latitude']) * converts

    lond = (lon2 - stations['longitude']) * converts

    clat = np.cos(lat2 * converts)

    slat = np.cos(stations['latitude'] * converts)

    first = 0.5 - np.cos(latd) / 2.0

    sec = slat * clat * (1 - np.cos(lond)) / 2.0

    result = first + sec
    
    result = np.clip(result, 0, 1) 

    return 12742 * np.arcsin(np.sqrt(result))


def best_tmax(city, stations):

    distances = distance(city, stations)  

    closest = np.argmin(distances)
    final = stations.loc[closest, 'avg_tmax']
    return final


datac['tavg'] = datac.apply(best_tmax, stations=stations, axis=1)

plt.figure(figsize=(8, 6))
plt.plot(datac['tavg'], datac['density'], 'b.', alpha=1)
plt.xlabel('Avg Max Temperature (\u00b0C)')
plt.ylabel('Population Density (people/km\u00b2)')
plt.title('Temperature vs Population Density')
plt.savefig('output.svg')




