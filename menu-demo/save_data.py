import json
import os


DATA_FILENAME = os.path.join(os.path.dirname(__file__), "coordinates.json")


def save_data(coordinates):
    """Save selected coordinates to a new or existing JSON file."""
    filename = input(
        f"File to save (blank for {DATA_FILENAME}): "
    ).strip().strip('"')

    if filename == "":
        filename = DATA_FILENAME

    if not os.path.isabs(filename) and os.path.dirname(filename) == "":
        filename = os.path.join(os.path.dirname(__file__), filename)

    while True:
        print("1. Append selected coordinates")
        print("2. Write selected coordinates (replace file contents)")
        mode = input("Save mode (1-2): ").strip()

        if mode == "1" or mode == "2":
            break

        print("Choose 1 or 2.")

    entries = list(coordinates.values())

    if len(entries) == 0:
        print("There are no coordinates to save.")
        return coordinates

    for index in range(len(entries)):
        coordinate = entries[index]
        print(
            f"{index + 1}. {coordinate['coordname']} "
            f"({coordinate['latitude']}, {coordinate['longitude']}) "
            f"order {coordinate['order']}"
        )

    selection_text = input(
        "Coordinate numbers separated by commas, or blank for all: "
    ).strip()

    if selection_text == "":
        selected_indexes = list(range(len(entries)))
    else:
        selected_indexes = []

        for value in selection_text.split(","):
            try:
                selected_index = int(value.strip()) - 1
            except ValueError:
                print("Enter coordinate numbers separated by commas.")
                return coordinates

            if selected_index < 0 or selected_index >= len(entries):
                print("A selected number is outside the displayed list.")
                return coordinates

            if selected_index not in selected_indexes:
                selected_indexes.append(selected_index)

    output_data = {}

    if mode == "1" and os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as coordinate_file:
                existing_data = json.load(coordinate_file)
        except (PermissionError, OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
            print(f"Could not read {filename}: {error}")
            return coordinates

        if not isinstance(existing_data, dict):
            print(f"A coordinate file must contain a JSON object: {filename}")
            return coordinates

        output_data.update(existing_data)

    skipped_names = []

    for selected_index in selected_indexes:
        coordinate = entries[selected_index]
        coordname = coordinate["coordname"]

        if mode == "1" and coordname in output_data:
            skipped_names.append(coordname)
            continue

        output_data[coordname] = {
            "coordname": coordname,
            "latitude": coordinate["latitude"],
            "longitude": coordinate["longitude"],
            "order": coordinate["order"],
        }

    try:
        with open(filename, "w", encoding="utf-8") as coordinate_file:
            json.dump(output_data, coordinate_file, indent=2)
            coordinate_file.write("\n")
    except (PermissionError, OSError) as error:
        print(f"Could not write {filename}: {error}")
        return coordinates

    saved_count = len(selected_indexes) - len(skipped_names)
    coordinate_label = "coordinate" if saved_count == 1 else "coordinates"
    print(
        f"Successfully saved {saved_count} {coordinate_label} "
        f"from selected data to {filename}."
    )

    if len(skipped_names) > 0:
        print(
            "Skipped existing coordinate name(s): "
            + ", ".join(skipped_names)
        )

    return coordinates
