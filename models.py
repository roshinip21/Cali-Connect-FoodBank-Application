# models.py

import pandas as pd
from sklearn.neighbors import NearestNeighbors
from geopy.distance import geodesic

def load_centers():
    """
    Returns a DataFrame of real California food-bank donation centers,
    with name, street address, and lat/lon.
    """
    return pd.DataFrame([
        {
            "name": "Los Angeles Regional Food Bank",
            "address": "2816 S Grand Ave, Los Angeles, CA 90007",
            "lat": 34.04481,
            "lon": -118.25782,
        },
        {
            "name": "San Diego Food Bank",
            "address": "9850 Distribution Ave, San Diego, CA 92121",
            "lat": 32.82310,
            "lon": -117.12595,
        },
        {
            "name": "Second Harvest Food Bank (Orange County)",
            "address": "8014 Marine Way, Irvine, CA 92618",
            "lat": 33.65303,
            "lon": -117.77099,
        },
        {
            "name": "Sacramento Food Bank & Family Services",
            "address": "3333 Third Ave, Sacramento, CA 95817",
            "lat": 38.56738,
            "lon": -121.46607,
        },
        {
            "name": "Food Bank of Contra Costa & Solano",
            "address": "4010 Nelson Ave, Concord, CA 94520",
            "lat": 37.98886,
            "lon": -122.01879,
        },
        {
            "name": "Food Bank of Santa Barbara County",
            "address": "1528 Chapala St, Santa Barbara, CA 93101",
            "lat": 34.42366,
            "lon": -119.70898,
        },
        {
            "name": "Feed the Hungry (Riverside)",
            "address": "2950 Jefferson St, Riverside, CA 92504",
            "lat": 33.99568,
            "lon": -117.37032,
        },
        {
            "name": "Redwood Empire Food Bank",
            "address": "3990 Atherton Rd, Santa Rosa, CA 95405",
            "lat": 38.47169,
            "lon": -122.69989,
        },
        {
            "name": "Alameda County Community Food Bank",
            "address": "7900 Edgewater Dr, Oakland, CA 94621",
            "lat": 37.70603,
            "lon": -122.19384,
        },
    ])

def build_knn_model(centers):
    """
    Fits a 1-NN model on center lat/lon.
    """
    model = NearestNeighbors(n_neighbors=1)
    model.fit(centers[['lat','lon']])
    return model

def find_nearest_center(model, centers, user_lat, user_lon):
    """
    Returns the nearest center row (with address) and the geodesic distance in km.
    """
    dist_matrix, idx = model.kneighbors([[user_lat, user_lon]])
    center = centers.iloc[idx[0][0]]
    km = geodesic((user_lat, user_lon), (center['lat'], center['lon'])).km
    return center, km
