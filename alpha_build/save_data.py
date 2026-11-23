import os

from list_data_files import list_data_files
from read_survey_file import read_survey_file
from select_coordinates import select_coordinates
from write_survey_file import write_survey_file


def save_data(state):
    """Save selected coordinates to a new or existing JSON file."""
    data_directory = list_data_files()

    if data_directory is None:
        return state

    default_filename = state["loaded_filename"]

    if default_filename is None:
        filename = input(
            "File to save (enter a listed filename or a new filename): "
        ).strip().strip('"')
    else:
        filename = input(
            f"File to save (blank for {default_filename}): "
        ).strip().strip('"')

        if filename == "":
            filename = default_filename

    if filename == "":
        print("A filename or path is required.")
        return state

    if not os.path.isabs(filename) and os.path.dirname(filename) == "":
        filename = os.path.join(data_directory, filename)

    while True:
        print("1. Append selected coordinates")
        print("2. Write selected coordinates (replace file contents)")
        mode = input("Save mode (1-2): ").strip()

        if mode == "1" or mode == "2":
            break

        print("Choose 1 or 2.")

    if mode == "2" and os.path.exists(filename):
        confirmation = input(
            f"Replace existing file {filename}? (y/n): "
        ).strip().lower()

        if confirmation not in ("y", "yes"):
            print("Replace cancelled.")
            return state

    selected_coordinates = select_coordinates(state, 1, "saving")

    if len(selected_coordinates) == 0:
        return state

    output_data = {}

    if mode == "1" and os.path.exists(filename):
        existing_data = read_survey_file(filename)

        if existing_data is None:
            return state

        output_data.update(existing_data)

    skipped_names = []

    for coordinate in selected_coordinates:
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

    if not write_survey_file(filename, output_data):
        return state

    state["loaded_filename"] = filename
    state["file_data"] = output_data
    saved_count = len(selected_coordinates) - len(skipped_names)
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

    return state
