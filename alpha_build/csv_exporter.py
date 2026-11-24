import csv
import os

def export_to_csv(coordinates, filename):
    """Exports a list of coordinate dictionaries to a CSV file."""
    if not coordinates:
        print("No coordinates provided to export.")
        return False

    # Ensure we are saving as .csv
    if not filename.endswith('.csv'):
        filename += '.csv'

    try:
        keys = ["coordname", "latitude", "longitude", "order"]
        with open(filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(coordinates)
        print(f"Successfully exported {len(coordinates)} coordinates to {filename}")
        return True
    except Exception as e:
        print(f"Failed to export CSV: {e}")
        return False
