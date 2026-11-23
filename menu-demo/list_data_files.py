import os


def list_data_files():
    """Display regular files in the project's data directory and return it."""
    project_directory = os.path.dirname(os.path.dirname(__file__))
    data_directory = os.path.join(project_directory, "data")

    try:
        os.makedirs(data_directory, exist_ok=True)
    except OSError as error:
        print(f"Could not create the data directory {data_directory}: {error}")
        return None

    try:
        filenames = sorted(os.listdir(data_directory))
    except OSError as error:
        print(f"Could not list files in {data_directory}: {error}")
        return None

    print("\nExisting files in data:")
    found_file = False

    for filename in filenames:
        file_path = os.path.join(data_directory, filename)

        if os.path.isfile(file_path):
            print(f"- {filename}")
            found_file = True

    if not found_file:
        print("(none)")

    return data_directory
