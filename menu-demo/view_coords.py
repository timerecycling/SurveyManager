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
        print(
            f"{coordinate['coordname']:<16}"
            f"{coordinate['latitude']:>14.6f}"
            f"{coordinate['longitude']:>16.6f}"
            f"{coordinate['order']:>10}"
        )
