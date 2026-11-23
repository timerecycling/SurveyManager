import math

from select_coordinates import select_coordinates


def calc_dist(state):
    """Sum great-circle distances between consecutive selected coordinates."""
    coordinates = select_coordinates(state, 2, "distance calculation")

    if len(coordinates) < 2:
        return None

    earth_radius_meters = 6371008.8
    total_distance = 0.0

    for index in range(len(coordinates) - 1):
        first = coordinates[index]
        second = coordinates[index + 1]
        first_latitude = math.radians(first["latitude"])
        second_latitude = math.radians(second["latitude"])
        latitude_difference = second_latitude - first_latitude
        longitude_difference = math.radians(
            second["longitude"] - first["longitude"]
        )
        haversine_value = (
            math.sin(latitude_difference / 2) ** 2
            + math.cos(first_latitude)
            * math.cos(second_latitude)
            * math.sin(longitude_difference / 2) ** 2
        )
        haversine_value = min(1.0, max(0.0, haversine_value))
        central_angle = 2 * math.atan2(
            math.sqrt(haversine_value),
            math.sqrt(1 - haversine_value),
        )
        total_distance += earth_radius_meters * central_angle

    if total_distance >= 1000:
        print(f"Total distance: {total_distance / 1000:.3f} km")
    else:
        print(f"Total distance: {total_distance:.2f} m")

    return total_distance
