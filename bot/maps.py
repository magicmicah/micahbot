import json
import requests
import settings

async def get_closest_place():

    # Define the Google Maps Places API endpoint
    api_endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

    # Define the search parameters
    params ={
        "location": "40.1282,-75.5145", # The latitude and longitude coordinates of Phoenixville, PA
        "radius": 5000, # The search radius (in meters) - adjust as needed
        "type": "restaurant", # Limit results to restaurants
        "keyword": "mcdonalds", # Search for McDonald's locations
        "key": settings.GOOGLE_MAPS_API_KEY
    }

    # Send the API request and parse the JSON response
    response = requests.get(api_endpoint, params=params)
    json()

    # Extract the relevant details for the closest McDonald's location
    mcdonalds = response["results"][0]
    name = mcdonalds["name"]
    address = mcdonalds["vicinity"]
    location = mcdonalds["geometry"]["location"]
    latitude = location["lat"]
    longitude = location["lng"]
    return (f"The closest McDonald's is {name}, located at {address}.")
