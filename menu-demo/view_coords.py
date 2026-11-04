# Print each coordinate record and all of its details.
def view_coords(coordinates):
    print("\nCoordinate       Latitude       Longitude       Order")
    print("-" * 58)

    for coordinate in coordinates.values():
        print(
            f"{coordinate['coordname']:<16}"
            f"{coordinate['latitude']:>14.6f}"
            f"{coordinate['longitude']:>16.6f}"
            f"{coordinate['order']:>10}"
        )
