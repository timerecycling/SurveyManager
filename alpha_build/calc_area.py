import math
from select_coordinates import select_coordinates

def spherical_area(coordinates):
    """Calculates the spherical area enclosed by three or more coordinates."""
    if len(coordinates) < 3:
        return None
    
    earth_radius_meters = 6371008.8
    longitude_latitude_sum = 0.0
    
    for index in range(len(coordinates)):
        first = coordinates[index]
        second = coordinates[(index + 1) % len(coordinates)]
        
        longitude_difference = math.radians(second["longitude"] - first["longitude"])
        
        # Handle wrap-around
        while longitude_difference > math.pi:
            longitude_difference -= 2 * math.pi
        while longitude_difference < -math.pi:
            longitude_difference += 2 * math.pi
            
        first_latitude = math.radians(first["latitude"])
        second_latitude = math.radians(second["latitude"])
        
        longitude_latitude_sum += longitude_difference * (
            2 + math.sin(first_latitude) + math.sin(second_latitude)
        )
        
    area_square_meters = abs(longitude_latitude_sum) * earth_radius_meters**2 / 2
    return area_square_meters

def calc_area(state):
    """Wrapper to calculate the spherical area enclosed by three or more coordinates."""
    coordinates = select_coordinates(state, 3, "area calculation")
    
    area = spherical_area(coordinates)
    if area is None:
        return None

    if area >= 1000000:
        print(f"Area: {area / 1000000:.3f} km^2")
    else:
        print(f"Area: {area:.2f} m^2")
        
    return area
