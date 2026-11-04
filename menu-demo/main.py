from add_or_update_coords import add_or_update_coords
from view_coords import view_coords

"""
Note: This dictionary starts at level 2 of the state machine.
"""
coordinates = {
    "Pine_1": {
        "coordname": "Pine_1",
        "latitude": 46.8705,
        "longitude": -113.994,
        "order": 1,
    },
    "River_1": {
        "coordname": "River_2",
        "latitude": 46.872,
        "longitude": -113.992,
        "order": 2,
    },
    "Stone_1": {
        "coordname": "Stone_3",
        "latitude": 46.869,
        "longitude": -113.996,
        "order": 3,
    },
}


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
        elif choice == "7":
            add_or_update_coords(coordinates)
        elif choice in ("2", "3", "4", "5", "6"):
            print("Coming soon")
        else:
            print("That option is not on the menu. Please choose again.")


if __name__ == "__main__":
    main()
