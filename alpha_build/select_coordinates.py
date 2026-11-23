def select_coordinates(state, minimum, purpose):
    """Prompt for a coordinate source and return selected records in order."""
    while True:
        print(f"\nSelect coordinates for {purpose}:")
        print("1. Session memory")
        print("2. Loaded file")
        print("3. Both")
        source_choice = input("Source (1-3): ").strip()

        if source_choice == "1":
            sources = ["memory"]
        elif source_choice == "2":
            sources = ["file_data"]
        elif source_choice == "3":
            sources = ["file_data", "memory"]
        else:
            print("Choose 1, 2, or 3.")
            continue

        entries = []

        for source in sources:
            for coordinate in state[source].values():
                entries.append((source, coordinate))

        if len(entries) == 0:
            print("There are no coordinates in that source.")
            return []

        for index in range(len(entries)):
            source, coordinate = entries[index]
            print(
                f"{index + 1}. [{source}] {coordinate['coordname']} "
                f"({coordinate['latitude']}, {coordinate['longitude']}) "
                f"order {coordinate['order']}"
            )

        selection_text = input(
            "Coordinate numbers, ranges, or 'all'; blank for all: "
        ).strip().lower()

        if selection_text == "" or selection_text == "all":
            selected_indexes = list(range(len(entries)))
        else:
            selected_indexes = []
            invalid_selection = False

            for value in selection_text.replace(" ", "").split(","):
                if "-" in value:
                    boundaries = value.split("-")

                    if len(boundaries) != 2:
                        print("Enter coordinate numbers separated by commas or ranges.")
                        invalid_selection = True
                        break

                    try:
                        start = int(boundaries[0])
                        end = int(boundaries[1])
                    except ValueError:
                        print("Enter coordinate numbers separated by commas or ranges.")
                        invalid_selection = True
                        break

                    if start < 1 or end < 1 or start > end:
                        print("A selected range is outside the displayed list.")
                        invalid_selection = True
                        break

                    range_indexes = range(start - 1, end)

                    if end > len(entries):
                        print("A selected number is outside the displayed list.")
                        invalid_selection = True
                        break

                    for selected_index in range_indexes:
                        if selected_index not in selected_indexes:
                            selected_indexes.append(selected_index)
                else:
                    try:
                        selected_index = int(value) - 1
                    except ValueError:
                        print("Enter coordinate numbers separated by commas or ranges.")
                        invalid_selection = True
                        break

                    if selected_index < 0 or selected_index >= len(entries):
                        print("A selected number is outside the displayed list.")
                        invalid_selection = True
                        break

                    if selected_index not in selected_indexes:
                        selected_indexes.append(selected_index)

            if invalid_selection:
                continue

        if len(selected_indexes) < minimum:
            print(f"Select at least {minimum} coordinate(s).")
            continue

        selected_coordinates = []

        for selected_index in selected_indexes:
            source, coordinate = entries[selected_index]
            selected_coordinates.append(coordinate)

        selected_coordinates.sort(key=lambda coordinate: coordinate["order"])
        return selected_coordinates
