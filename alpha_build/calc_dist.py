import math
from select_coordinates import select_coordinates

def haversine_distance(coord1, coord2):
    """Calculates Haversine distance between two points in meters."""
    earth_radius_meters = 6371008.8
    lat1, lon1 = math.radians(coord1["latitude"]), math.radians(coord1["longitude"])
    lat2, lon2 = math.radians(coord2["latitude"]), math.radians(coord2["longitude"])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return earth_radius_meters * c

def calc_dist(state):
    """Sum great-circle distances between consecutive selected coordinates."""
    coordinates = select_coordinates(state, 2, "distance calculation")
    if len(coordinates) < 2:
        return None

    total_distance = 0.0
    for i in range(len(coordinates) - 1):
        total_distance += haversine_distance(coordinates[i], coordinates[i+1])

    if total_distance >= 1000:
        print(f"Total distance: {total_distance / 1000:.3f} km")
    else:
        print(f"Total distance: {total_distance:.2f} m")

    return total_distance
