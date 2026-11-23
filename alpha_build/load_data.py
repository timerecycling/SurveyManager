# loads coordinates from a JSON file and returns them as a dictionary

import json
import os

DATA_FILENAME = os.path.join(os.path.dirname(__file__), "coordinates.json")


def load_data(filename=None):
    if filename is None:
        filename = input(
            "File to load (enter a filename or path): "
        ).strip().strip('"')

        if filename == "":
            print("A filename or path is required.")
            return None

    if not os.path.isabs(filename) and os.path.dirname(filename) == "":
        filename = os.path.join(os.path.dirname(__file__), filename)

    try:
        with open(filename, "r", encoding="utf-8") as coordinate_file:
            coordinates = json.load(coordinate_file)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except (PermissionError, OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        print(f"Could not read {filename}: {error}")
        return None

    if not isinstance(coordinates, dict):
        print(f"A coordinate file must contain a JSON object: {filename}")
        return None

    coordinate_label = "coordinate" if len(coordinates) == 1 else "coordinates"
    print(f"Successfully loaded {len(coordinates)} {coordinate_label} from {filename}.")
    return coordinates
