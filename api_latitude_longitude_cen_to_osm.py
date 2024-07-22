# latitude and longitude of the center point and want to fetch OSM data for a bounding box area around this center point, you can calculate the bounding box coordinates based on a specified radius. Here's how you can modify the Python script to achieve this:

# Python Script to Fetch .osm File for Bounding Box Area around Center Point

import requests
from math import radians, cos, sin, sqrt

def fetch_osm_bbox_data(center_lat, center_lon, radius):
    overpass_url = "http://overpass-api.de/api/interpreter"
    
    # Validate latitude and longitude inputs
    if not (-90.0 <= center_lat <= 90.0):
        raise ValueError("Latitude must be between -90.0 and 90.0 degrees")
    if not (-180.0 <= center_lon <= 180.0):
        raise ValueError("Longitude must be between -180.0 and 180.0 degrees")
    
    # Calculate bounding box coordinates
    earth_radius = 111000.0  # Earth's radius in meters
    delta_lat = radius / earth_radius
    delta_lon = radius / (earth_radius * cos(radians(center_lat)))
    
    min_lat = center_lat - delta_lat
    max_lat = center_lat + delta_lat
    min_lon = center_lon - delta_lon
    max_lon = center_lon + delta_lon
    
    # Construct Overpass QL query
    overpass_query = f"""
        [out:xml];
        (
            node({min_lat},{min_lon},{max_lat},{max_lon});
            way["highway"~"motorway|trunk|primary|secondary|tertiary|unclassified|residential|service"]({min_lat},{min_lon},{max_lat},{max_lon});
            relation["type"="route"]["route"="road"]({min_lat},{min_lon},{max_lat},{max_lon});
        );
        out meta;
        >;
        out skel qt;
    """

    # bbox = (min_lat,min_lon,max_lat,max_lon)
    # bbox_str = ",".join(map(str, bbox))
    # overpass_query = overpass_query.format(bbox=bbox_str)


    response = requests.get(overpass_url, params={'data': overpass_query})
    
    if response.status_code == 200:
        filename = f"osm_bbox_data_{center_lat}_{center_lon}_{radius}.osm"
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"OSM data saved to {filename}")
    else:
        print(f"Error fetching data from Overpass API: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    try:
        # Example: Input center point coordinates and radius in meters
        # center_lat = float(input("Enter Latitude of center point: "))
        # center_lon = float(input("Enter Longitude of center point: "))
        # radius = float(input("Enter radius in meters: "))
        center_lon =116.397455
        center_lat =39.909187
        radius =500
        fetch_osm_bbox_data(center_lat, center_lon, radius)
    except ValueError as e:
        print(f"Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

    
    # Example: Input center point coordinates and radius in meters
    # center_lat = float(input("Enter Latitude of center point: "))
    # center_lon = float(input("Enter Longitude of center point: "))
    # radius = float(input("Enter radius in meters: "))




# Explanation:
# calculate_bbox function:

# Takes the center latitude (center_lat), center longitude (center_lon), and radius (radius) in meters as inputs.
# Converts radius to degrees and calculates the bounding box corners (min_lat, min_lon, max_lat, max_lon) around the center point.
# Uses the Haversine formula to calculate the bounding box coordinates based on the specified radius.
# fetch_osm_bbox_data function:

# Calls calculate_bbox to compute the bounding box coordinates based on the center point and radius.
# Constructs an Overpass QL query (overpass_query) to fetch nodes, ways, and relations within the computed bounding box.
# Sends a GET request to the Overpass API (overpass_url) with the constructed query.
# If the request is successful (status code 200), it saves the XML response content directly to a .osm file named osm_bbox_data_{center_lat}_{center_lon}_{radius}.osm.
# If there's an error (status code not 200), it prints an error message.
# Main script:

# Prompts the user to input the latitude and longitude of the center point and the radius in meters.
# Calls the fetch_osm_bbox_data function with the provided inputs.
# Notes:
# Haversine Formula: The script uses an approximation to calculate the bounding box coordinates based on the specified radius around the Earth's surface. This approximation is suitable for smaller distances and may not be perfectly accurate for very large radii or near the poles.

# Overpass Query: Adjust the query (overpass_query) as needed to fetch specific types of data (node, way, relation) or add additional filters based on your requirements.

# File Naming: The generated .osm file is named based on the center latitude, longitude, and radius to avoid overwriting existing files and to keep track of different queries.

# This script provides a flexible way to fetch OSM data for a bounding box area around a center point defined by latitude and longitude inputs. Adjustments can be made based on specific use cases or additional requirements for the data query or output format.