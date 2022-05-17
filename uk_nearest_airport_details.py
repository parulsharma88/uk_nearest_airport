import pandas as pd

from math import radians, cos, sin, asin, sqrt


def distance_between_user_and_airport(user_latitude, user_longitude, airport_latitude, airport_longitude):
    """
    Calculate the great circle distance between two coordinates
    on the earth (specified in decimal degrees)
    """
    # convert coordinates to radians
    user_latitude, user_longitude, airport_latitude, airport_longitude = map(radians, [user_latitude, user_longitude,
                                                                                       airport_latitude,
                                                                                       airport_longitude])
    # haversine formula
    dlon = airport_longitude - user_longitude
    dlat = airport_latitude - user_latitude
    a = sin(dlat/2)**2 + cos(user_latitude) * cos(airport_latitude) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    km = 6371 * c
    miles = km * 0.62
    return round(miles, 3)


def find_nearest_airport(latitude, longitude):
    distances = airports.apply(lambda row: distance_between_user_and_airport(latitude, longitude, row['Latitude'],
                                                                             row['Longitude']), axis=1)
    nearest_airport_details = [airports.loc[distances.idxmin(), 'NAME'], distances[distances.idxmin()]]
    return nearest_airport_details


try:
    latitude = input('Please enter the latitude:- ')
    if not latitude:
        raise ValueError('Empty Latitude. Please enter some value.')
    elif latitude < '0':
        raise ValueError('Latitude should always be positive value')
    longitude = float(input('Please enter the longitude:- '))
    if not longitude:
        raise ValueError('Empty Longitude. Please enter some value.')

    airports = pd.read_csv(r'uk_airport_coords.csv')

    nearest_airport = find_nearest_airport(float(latitude), float(longitude))

    print('Nearest Airport is ', nearest_airport[0], ' which is ', nearest_airport[1], ' miles away.') 

except ValueError as e:
    print(e)
