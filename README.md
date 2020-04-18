# Fetching Daily Temperature Data from Dark Sky API

In this project, I fetch the daily minimum and maximum temperatures for 17 cities from the [Dark Sky API](https://darksky.net/dev). I use Angel Hernandez's [Python 3 Dark Sky Wrapper Library](https://github.com/bitpixdigital/forecastiopy3) to communicate to the API. The data is fetched for the latest set of 5 consecutive days and the average daily minimum and maximum temperatures are calculated. Finally, the output is stored in the CSV format with accuracy of 2 decimal places.

List of cities (and their corresponding latitudes and longitudes):

| City                           | Latitude  | Longitude  |
|:-------------------------------|----------:|-----------:|
| Anchorage, Alaska              | 61.2181   | -149.9003  |
| Bishkek, Kyrgyzstan            | 42.8746   | 74.5698    |
| Buenos Aires, Argentina        | -34.6037  | -58.3816   |
| Dhahran, Saudia Arabia         | 26.2361   | 50.0393    |
| Giza, Egypt                    | 30.0131   | 31.2089    |
| Hyderabad, India               | 17.385    | 78.4867    |
| Madrid, Spain                  | 40.4168   | -3.7038    |
| Mannheim, Germany              | 49.4875   | 8.466      |
| Nanaimo, Canada                | 49.1659   | -123.9401  |
| Ningbo, China                  | 29.8683   | 121.544    |
| Oldham, United Kingdom         | 53.5409   | -2.1114    |
| Quetta, Pakistan               | 30.1798   | 66.975     |
| Riga, Latvia                   | 56.9496   | 24.1052    |
| San José, California           | 9.9281    | -84.0907   |
| São José dos Campos, Brazil    | -23.2237  | -45.9009   |
| Tehran, Iran                   | 35.6892   | 51.389     |
| Warsaw, Poland                 | 52.2297   | 21.0122    |