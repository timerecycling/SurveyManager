from select_coordinates import select_coordinates


def view_coords(state):
    """Display selected coordinate records from session or file data."""
    coordinates = select_coordinates(state, 1, "viewing")

    if len(coordinates) == 0:
        print("No coordinates to display.")
        return

    coordinate_label = "coordinate" if len(coordinates) == 1 else "coordinates"
    print(f"\nDisplaying {len(coordinates)} {coordinate_label}.")
    print("Coordinate       Latitude       Longitude       Order")
    print("-" * 58)

    for coordinate in coordinates:
        print(
            f"{coordinate['coordname']:<16}"
            f"{coordinate['latitude']:>14.6f}"
            f"{coordinate['longitude']:>16.6f}"
            f"{coordinate['order']:>10}"
        )
