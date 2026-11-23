<<<<<<< HEAD
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
=======
#prints all coordinates or a comma-separated selection by name
def view_coords(coordinates):
    selection = input(
        "Coordinate names separated by commas, or blank for all: "
    ).strip()

    if selection == "":
        selected_coordinates = list(coordinates.values())
    else:
        selected_names = []

        for value in selection.split(","):
            coordname = value.strip()

            if coordname == "" or coordname not in coordinates:
                print(f"Unknown coordinate name: {coordname}")
                return

            if coordname not in selected_names:
                selected_names.append(coordname)

        selected_coordinates = []

        for coordname in selected_names:
            selected_coordinates.append(coordinates[coordname])

    print("\nCoordinate       Latitude       Longitude       Order")
    print("-" * 58)

    for coordinate in selected_coordinates:
>>>>>>> ea4cec2ed132c15988aa1be6669d774ae1cc67e7
        print(
            f"{coordinate['coordname']:<16}"
            f"{coordinate['latitude']:>14.6f}"
            f"{coordinate['longitude']:>16.6f}"
            f"{coordinate['order']:>10}"
        )
