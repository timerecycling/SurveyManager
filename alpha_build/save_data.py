import os
import json
from list_data_files import list_data_files
from read_survey_file import read_survey_file
from select_coordinates import select_coordinates
from write_survey_file import write_survey_file
from csv_exporter import export_to_csv
from validator import validate_survey_data

def save_data(state):
    """Save or export coordinates from session memory."""
    data_directory = list_data_files()

    if data_directory is None:
        return state

    default_filename = state.get("loaded_filename")

    if default_filename is None:
        filename = input(
            "File to save (enter a name or path): "
        ).strip().strip('\"')
    else:
        filename = input(
            f"File to save (blank for {default_filename}): "
        ).strip().strip('\"')
        if filename == "":
            filename = default_filename

    if not filename:
        print("A filename is required.")
        return state

    if not os.path.isabs(filename) and os.path.dirname(filename) == "":
        filename = os.path.join(data_directory, filename)

    print("\nSelect action:")
    print("1. Append to JSON")
    print("2. Write to JSON (replace contents)")
    print("3. Export to CSV")
    mode = input("Select mode (1-3): ").strip()

    if mode not in ("1", "2", "3"):
        print("Invalid mode.")
        return state

    # Selection of data
    selected_coordinates = select_coordinates(state, 1, "saving")
    if not selected_coordinates:
        print("No coordinates selected.")
        return state

    # Option 3: CSV Export
    if mode == "3":
        if export_to_csv(selected_coordinates, filename):
            state["loaded_filename"] = filename
        return state

    # JSON Operations (Modes 1 & 2)
    output_data = {}
    if mode == "1" and os.path.exists(filename):
        existing_data = read_survey_file(filename)
        if existing_data:
            output_data.update(existing_data)

    # Option 2: Preview for overwrite
    if mode == "2" and os.path.exists(filename):
        print(f"\n--- PREVIEW: Current contents of {filename} ---")
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                preview_data = json.load(f)
            for k, v in list(preview_data.items())[:3]:
                print(f"  {k}: {v}")
            if len(preview_data) > 3:
                print("  ...")
        except Exception:
            print("  [Could not preview existing file content]")
        
        confirm = input("\nOverwriting this file. Proceed? (y/n): ").strip().lower()
        if confirm not in ("y", "yes"):
            print("Operation cancelled.")
            return state

    # Build the output dictionary
    skipped_names = []
    for coord in selected_coordinates:
        name = coord["coordname"]
        if mode == "1" and name in output_data:
            skipped_names.append(name)
            continue
        output_data[name] = {
            "coordname": name,
            "latitude": coord["latitude"],
            "longitude": coord["longitude"],
            "order": coord["order"],
        }

    # Validation
    is_valid, err_msg = validate_survey_data(output_data)
    if not is_valid:
        print(f"Validation Error: {err_msg}")
        return state

    # Write to file
    if write_survey_file(filename, output_data):
        state["loaded_filename"] = filename
        state["file_data"] = output_data
        print(f"Successfully saved to {filename}")
        if skipped_names:
            print(f"Skipped existing names: {', '.join(skipped_names)}")
    
    return state
