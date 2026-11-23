import math


def input_coords(state):
    """Add or update decimal-degree coordinate records in session memory."""
    print("Enter coordinate names and decimal-degree coordinates.")
    print("Enter 0 as the coordinate name when you are finished.")

    while True:
        coordname = input("Coordinate name: ").strip()

        if coordname == "":
            print("Coordinate name cannot be blank.")
            continue

        if coordname == "0":
            break

        if "," in coordname:
            print("Coordinate names cannot contain commas.")
            continue

        existing = state["memory"].get(coordname)

        if existing is not None:
            update = input(f"Update existing coordinate {coordname}? (y/n): ").strip().lower()

            if update not in ("y", "yes"):
                print(f"Keeping existing coordinate {coordname}.")
                continue

            print(f"Updating {coordname}.")
        else:
            print(f"Adding {coordname}.")

        while True:
            latitude_text = input("Latitude (-90 to 90): ").strip()

            try:
                latitude = float(latitude_text)
            except ValueError:
                print("Enter a valid number for latitude.")
                continue

            if not math.isfinite(latitude) or latitude < -90 or latitude > 90:
                print("Latitude must be between -90 and 90.")
                continue

            break

        while True:
            longitude_text = input("Longitude (-180 to 180): ").strip()

            try:
                longitude = float(longitude_text)
            except ValueError:
                print("Enter a valid number for longitude.")
                continue

            if not math.isfinite(longitude) or longitude < -180 or longitude > 180:
                print("Longitude must be between -180 and 180.")
                continue

            break

        if existing is not None:
            order = existing["order"]
        else:
            order = 1

            for coordinate in state["memory"].values():
                if coordinate["order"] >= order:
                    order = coordinate["order"] + 1

        state["memory"][coordname] = {
            "coordname": coordname,
            "latitude": latitude,
            "longitude": longitude,
            "order": order,
        }

        if existing is not None:
            print(f"Successfully updated {coordname}.")
        else:
            print(f"Successfully added {coordname} to session memory.")

    return state

