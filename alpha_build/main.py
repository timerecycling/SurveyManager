<<<<<<< HEAD
from create_state import create_state
from calc_area import calc_area
from calc_dist import calc_dist
from input_coords import input_coords
=======
import os

from add_or_update_coords import add_or_update_coords
>>>>>>> ea4cec2ed132c15988aa1be6669d774ae1cc67e7
from load_data import load_data
from save_data import save_data
from view_coords import view_coords

<<<<<<< HEAD
=======

DATA_FILENAME = os.path.join(os.path.dirname(__file__), "coordinates.json")


# Load coordinates from the data file at startup. If the file doesn't exist, start with an empty dictionary.
coordinates = load_data(DATA_FILENAME)
>>>>>>> ea4cec2ed132c15988aa1be6669d774ae1cc67e7

def main():
    """Run the interactive survey-tool menu."""
    state = create_state()

    while True:
        print("\nWaldo's Locate & Survey")
        print("1. View Coordinates")
        print("2. Distance")
        print("3. Area")
        print("4. Geofence")
        print("5. Load Data")
        print("6. Save Coordinates")
        print("7. Input Coordinates")
        print("0. Exit")
        choice = input("Select an option's #: ").strip()

        if choice == "1":
            view_coords(state)
        elif choice == "2":
            calc_dist(state)
        elif choice == "3":
            calc_area(state)
        elif choice == "4":
            geofence(state)
        elif choice == "5":
            load_data(state)
        elif choice == "6":
            save_data(state)
        elif choice == "7":
            input_coords(state)
        elif choice == "0":
            print("Goodbye.")
            break
<<<<<<< HEAD
=======
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
>>>>>>> ea4cec2ed132c15988aa1be6669d774ae1cc67e7
        else:
            print("That option is not on the menu. Please choose again.")


if __name__ == "__main__":
    main()
