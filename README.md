# SurveyManager
Command line utility for managing coordinate-pair lists and producing survey products. 

# Business Problem
A survey company has been using pen & paper for recording data, and doing most processing tasks using manual entry on a laptop. Th#s app puts everything onto a laptop in a simple text interface, simplifying job tasks for surveyors.

# Business Question (Functionality not yet implemented)
How can we produce useful survey products using a simple python program?

# How to run
- Clone or download a .zip archive of the repository from Github
- Run 'main.py'
- Choose a menu option. Some options display, but don't function yet. Stay tuned!

# Menu Options (Nonfunctional options ommitted)
1. View Coordinates
5. Load Data
6. Save Coordinates
7. Input Coordinates
0. Exit

# Files 
- 'main.py' - main menu loop
- 'calc_area.py' - calculates area of a polygon from three or more coordinate pairs.
- 'calc_dist.py' - calculates distances from two or more coordinate pairs.
- 'create_state.py' - creates the state dictionary structure for memory.
- 'input_coords.py' - prompts the user to input coordinate pairs. can overwrite existing pairs.
- 'list_data_files.py' - called by 'save_data.py' to enumerate the data directory for the program.
- 'load_data.py' - loads data from a JSON file. WARNING: This replaces the coordinates in memory.
- 'save_data.py' - saves data to a JSON file. Write or append and select specific entries from memory (or all).
- 'read_survey_file.py' - called by 'save_data.py' to read a selected JSON file pending write to detect malformed data.
- 'select_coordinates.py' - called when coordinates must be chosen such as in both calc_X.py functions.
- 'view_coords.py' - prints desired coordinates in a table format
- 'write_survey_file.py' - called by 'save_data.py' to write data to the desired file. 

# Author
Jesse
