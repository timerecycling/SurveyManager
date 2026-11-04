# Asks for a coordinate name, updates an existing record or adds a new one. 
# Uses try statements for error handling and input validation.

def add_or_update_coords(coordinates):
    coord_updated = False
    coordname = input("Coordinate name: ").strip()

    if coordname == "":
        print("Coordinate name cannot be blank.")
        return

    if coordname in coordinates:
        coord_updated = True
        print(f"Updating {coordname}.")
    else:
        print(f"Adding {coordname}.")

    while True:
        latitude_text = input("Latitude (-90 to 90): ").strip()

        try:
            latitude = float(latitude_text)
        except ValueError:
            print("Enter a valid number for latitude. Ex: 46.8705")
            continue

        if latitude < -90 or latitude > 90:
            print("Latitude must be between -90 and 90.")
            continue

        break

    while True:
        longitude_text = input("Longitude (-180 to 180): ").strip()

        try:
            longitude = float(longitude_text)
        except ValueError:
            print("Enter a valid number for longitude. Ex: -113.994")
            continue

        if longitude < -180 or longitude > 180:
            print("Longitude must be between -180 and 180.")
            continue

        break

    if coordname in coordinates:
        order = coordinates[coordname]["order"]
    else:
        order = len(coordinates) + 1

    coordinates[coordname] = {
        "coordname": coordname,
        "latitude": latitude,
        "longitude": longitude,
        "order": order,
    }
    if coord_updated == True:
        print(f"Successfully updated {coordname}.")
    else:
        print(f"Successfully added {coordname}.")
