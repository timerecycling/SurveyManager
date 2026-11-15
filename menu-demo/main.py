import os

from add_or_update_coords import add_or_update_coords
from load_data import load_data
from save_data import save_data
from view_coords import view_coords


DATA_FILENAME = os.path.join(os.path.dirname(__file__), "coordinates.json")


# Load coordinates from the data file at startup. If the file doesn't exist, start with an empty dictionary.
coordinates = load_data(DATA_FILENAME)


# Print menu options, even unimplemented ones.
def show_menu():
    print("\nWaldo's Locate & Survey")
    print("1. View Coordinates")
    print("2. Distance")
    print("3. Area")
    print("4. Geofence")
    print("5. Load Data")
    print("6. Save Coordinates")
    print("7. Input Coordinates")
    print("0. Exit")


# Keep showing the menu until an option is selected.
def main():
    while True:
        show_menu()
        choice = input("Select an option's #: ").strip()

        if choice == "0":
            print("Goodbye.")
            break
        elif choice == "1":
            view_coords(coordinates)
        elif choice == "5":
            loaded_coordinates = load_data()

            if loaded_coordinates is not None:
                coordinates.clear()
                coordinates.update(loaded_coordinates)
        elif choice == "6":
            save_data(coordinates)
        elif choice == "7":
            add_or_update_coords(coordinates)
        elif choice in ("2", "3", "4"):
            print("Coming soon")
        else:
            print("That option is not on the menu. Please choose again.")


if __name__ == "__main__":
    main()
