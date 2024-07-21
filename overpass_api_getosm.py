import requests


# To achieve this task in Python, you can use the requests library to interact with the Overpass API and retrieve OpenStreetMap data based on the provided latitude and longitude coordinates. Here's a step-by-step Python script that demonstrates how to do this:

# Install the requests library: If you haven't already installed the requests library, you can install it using pip:

# pip install requests
# Python script: Create a Python script with the following code. This script takes latitude and longitude as input, forms a query for Overpass API, sends a request to Overpass, and saves the OSM XML response to a file.


def fetch_osm_data(latitude, longitude, radius=1000):
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
        [out:xml];
        (
            node["place"](around:{radius},{latitude},{longitude});
            way["place"](around:{radius},{latitude},{longitude});
            relation["place"](around:{radius},{latitude},{longitude});
        );
        out meta;
    """
    
    response = requests.get(overpass_url, params={'data': overpass_query})
    
    if response.status_code == 200:
        filename = f"osm_data_{latitude}_{longitude}.osm"
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"OSM data saved to {filename}")
    else:
        print(f"Error fetching data from Overpass API: {response.status_code}")

if __name__ == "__main__":
    latitude = input("Enter Latitude: ")
    longitude = input("Enter Longitude: ")
    
    fetch_osm_data(latitude, longitude)


# Explanation:
# Function fetch_osm_data:

# Constructs an Overpass QL query (overpass_query) to fetch nodes, ways, and relations tagged with "place" within a specified radius (default is 1000 meters) around the provided latitude and longitude.
# Sends a GET request to the Overpass API (overpass_url) with the constructed query.
# If the request is successful (status code 200), it saves the XML response content directly to a .osm file named osm_data_{latitude}_{longitude}.osm.
# If there's an error (status code not 200), it prints an error message.
# Main script:

# Prompts the user to input latitude and longitude.
# Calls the fetch_osm_data function with the provided latitude and longitude.
# Notes:
# The Overpass QL query in overpass_query specifies to retrieve nodes, ways, and relations tagged with "place" within the specified radius around the latitude and longitude coordinates.
# The output file name (osm_data_{latitude}_{longitude}.osm) includes the latitude and longitude in the file name to make it unique.
# This script assumes that the Overpass API is accessible and the request format ([out:xml];) and query structure (node["place"](around:1000,latitude,longitude);) are correctly formatted for your use case.
# Make sure to handle exceptions and errors as per your application's requirements, especially if integrating this into a larger system or automation workflow.