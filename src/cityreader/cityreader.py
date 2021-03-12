import csv
import pandas as pd

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

class City():
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
    # def __str__(self):
        # return f"{self.name}, {self.lat}, {self.lon}"
    def __repr__(self):
        return f"{self.name}, {self.lat}, {self.lon}"



cities = []

def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # Ensure that the lat and lon valuse are all floats
    # For each city record, create a new City instance and add it to the 
    # `cities` list

# -------------
    # fields = []
    # rows = []

    # with open('cities.csv', 'r') as file:
    #     reader = csv.reader(file)

    #     fields = next(reader)
    #     for row in reader:
    #         rows.append(row)
    
    # print(f"Field names are {[field for field in fields]}")

    # print([f"{row}" for row in rows[:3]])
# -------------
    # fields = []
    # with open('cities.csv', 'r') as in_file:
    #     reader = csv.reader(in_file)
    #     fields = next(reader)
    #     cities_dict = {rows[0] for rows in reader}

    #     print(cities_dict)
# -------------

    # df = pd.DataFrame([[],[]])
    df = pd.read_csv('cities.csv')

    dict_list = []

    # #iterate over each row in df
    for i in df.index:

        #create empty dictionary for each row
        dict_row = {}

        # populate 
        dict_row['name'] = df.at[i, 'city']
        dict_row['lat'] = df.at[i, 'lat']
        dict_row['lon'] = df.at[i, 'lng']

        # append
        dict_list.append(dict_row)
        # print(dict_list)

    for i in dict_list:
        new_city = City(i['name'],i['lat'],i['lon'])
        cities.append(new_city)
        # print(new_city)

    print(cities)
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
# for c in cities:
    # print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

# def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
#     # within will hold the cities that fall within the specified region
#     within = []
    
#     # Go through each city and check to see if it falls within 
#     # the specified coordinates.

#     return within