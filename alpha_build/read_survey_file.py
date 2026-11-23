import json
import math


def _reject_duplicate_keys(pairs):
    """Build a JSON object while rejecting repeated keys."""
    data = {}

    for key, value in pairs:
        if key in data:
            raise ValueError(f"Duplicate JSON key: {key}")

        data[key] = value

    return data


def read_survey_file(filename):
    """Read and validate a JSON coordinate file, returning None on failure."""
    try:
        with open(filename, "r", encoding="utf-8") as survey_file:
            data = json.load(
                survey_file,
                object_pairs_hook=_reject_duplicate_keys,
            )
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except PermissionError:
        print(f"Permission denied while reading: {filename}")
        return None
    except json.JSONDecodeError as error:
        print(f"Invalid JSON in {filename}: {error}")
        return None
    except ValueError as error:
        print(f"Invalid JSON in {filename}: {error}")
        return None
    except UnicodeDecodeError as error:
        print(f"Could not decode {filename} as UTF-8: {error}")
        return None
    except OSError as error:
        print(f"Could not read {filename}: {error}")
        return None

    if not isinstance(data, dict):
        print("A survey file must contain a JSON object.")
        return None

    for coordname, coordinate in data.items():
        if not isinstance(coordname, str) or not isinstance(coordinate, dict):
            print("Each survey entry must be an object keyed by coordinate name.")
            return None

        if coordinate.get("coordname") != coordname:
            print(f"Coordinate key and coordname must match for {coordname}.")
            return None

        latitude = coordinate.get("latitude")
        longitude = coordinate.get("longitude")
        order = coordinate.get("order")

        if (
            isinstance(latitude, bool)
            or not isinstance(latitude, (int, float))
            or isinstance(longitude, bool)
            or not isinstance(longitude, (int, float))
            or isinstance(order, bool)
            or not isinstance(order, int)
        ):
            print(f"Invalid coordinate values for {coordname}.")
            return None

        if (
            not math.isfinite(latitude)
            or not math.isfinite(longitude)
            or latitude < -90
            or latitude > 90
            or longitude < -180
            or longitude > 180
        ):
            print(f"Coordinates are outside valid ranges for {coordname}.")
            return None

        coordinate["latitude"] = float(latitude)
        coordinate["longitude"] = float(longitude)

    return data
