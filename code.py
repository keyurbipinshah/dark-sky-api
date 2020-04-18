# Loading packages --------------------------------------------------
from forecastiopy import *
from datetime import datetime
import pandas as pd
import numpy as np
import os

# Dark Sky API Key
api_file = open(".env")
api_key = api_file.readline()

# Geocodes of cities for which data is to be requested --------------
city_geo = {"Anchorage, Alaska": [61.2181, -149.9003],
            "Buenos Aires, Argentina": [-34.6037, -58.3816],
            "São José dos Campos, Brazil": [-23.2237, -45.9009],
            "San José, California": [9.9281, -84.0907],
            "Nanaimo, Canada": [49.1659, -123.9401],
            "Ningbo, China": [29.8683, 121.5440],
            "Giza, Egypt": [30.0131, 31.2089],
            "Mannheim, Germany": [49.4875, 8.4660],
            "Hyderabad, India": [17.3850, 78.4867],
            "Tehran, Iran": [35.6892, 51.3890],
            "Bishkek, Kyrgyzstan": [42.8746, 74.5698],
            "Riga, Latvia": [56.9496, 24.1052],
            "Quetta, Pakistan": [30.1798, 66.9750],
            "Warsaw, Poland": [52.2297, 21.0122],
            "Dhahran, Saudia Arabia": [26.2361, 50.0393],
            "Madrid, Spain": [40.4168, -3.7038],
            "Oldham, United Kingdom": [53.5409, -2.1114]}

# To change city list, follow the format "<city_name>": [latitude, longitude]
# in the manner defined above between braces.
# No other part of the program needs to be modified

# Extracting the latitudes as a dictionary from city_geo ------------
latitudes = {city: city_geo[city][0] for city in city_geo}

# Extracting the longitudes as a dictionary from city_geo -----------
longitudes = {city: city_geo[city][1] for city in city_geo}

# Fetching data from Dark Sky API -----------------------------------

# Initializing a blank dictionary to store city names along with minimum and
# maximum temperatures for next five days
dat = {"city": [],
       "min1": [],
       "max1": [],
       "min2": [],
       "max2": [],
       "min3": [],
       "max3": [],
       "min4": [],
       "max4": [],
       "min5": [],
       "max5": []}

# Looping over each city x day and executing data fetching code from
# bitpixdigital/forecastiopy3/README.md
for city in city_geo.keys():
    dat["city"].append(city)
    weather = ForecastIO.ForecastIO(api_key,
                                    latitude = latitudes[city],
                                    longitude = longitudes[city])
    daily = FIODaily.FIODaily(weather)
    for day in range(2, 7):
        val = daily.get_day(day)
        dat["min" + str(day - 1)].append(val["temperatureMin"])
        dat["max" + str(day - 1)].append(val["temperatureMax"])

# Converting the dictionary into a pandas DataFrame object
df = pd.DataFrame(dat)

# Computing the averages of minimum temperatures, round the average to
# two decimal places
df["min_avg"] = (df["min1"] +
                 df["min2"] +
                 df["min3"] +
                 df["min4"] +
                 df["min5"]) / 5
df["min_avg"] = df["min_avg"].apply(func = lambda x: "{temp: .2f}".format(temp = x))
  
# Computing the averages of maximum temperatures, rounding the average to
# two decimal places
df["max_avg"] = (df["max1"] +
                 df["max2"] +
                 df["max3"] +
                 df["max4"] +
                 df["max5"]) / 5
df["max_avg"] = df["max_avg"] = df["max_avg"].apply(func = lambda x: "{temp: .2f}".format(temp = x))
  
# Writing the DataFrame object to a comma-separated text file
df.to_csv("temperatures.csv",
          sep = ",",
          na_rep = "",
          index = False,
          header = ["City",
                    "Min 1", "Max 1",
                    "Min 2", "Max 2",
                    "Min 3", "Max 3",
                    "Min 4", "Max 4",
                    "Min 5", "Max 5",
                    "Min Avg", "Max Avg"])
