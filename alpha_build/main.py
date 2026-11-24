from create_state import create_state
from calc_area import calc_area
from calc_dist import calc_dist
from input_coords import input_coords
from load_data import load_data
from save_data import save_data
from view_coords import view_coords


def main():
    """Run the interactive survey-tool menu."""
    state = create_state()

    while True:
        print("\nWaldo's Locate & Survey")
        print("1. View Coordinates")
        print("2. Distance")
        print("3. Area")
        print("[Not Yet Implemented] 4. Geofence")
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
            print("Geofence is not yet implemented.")
        elif choice == "5":
            data, fname = load_data()
            if data:
                state["memory"] = data
                state["loaded_filename"] = fname
        elif choice == "6":
            save_data(state)
        elif choice == "7":
            input_coords(state)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("That option is not on the menu. Please choose again.")


if __name__ == "__main__":
    main()
