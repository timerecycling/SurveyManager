def validate_survey_data(data):
    """
    Validates that the data is a dictionary of coordinate records.
    Each record must have 'coordname', 'latitude', and 'longitude' with valid numeric values.
    """
    if not isinstance(data, dict):
        return False, "Data is not a dictionary."

    for name, coord in data.items():
        if not isinstance(coord, dict):
            return False, f"Record '{name}' is not a dictionary."
        
        required_keys = ["coordname", "latitude", "longitude"]
        if not all(k in coord for k in required_keys):
            return False, f"Record '{name}' is missing required keys {required_keys}."
        
        try:
            float(coord["latitude"])
            float(coord["longitude"])
        except (ValueError, TypeError):
            return False, f"Record '{name}' has non-numeric coordinates."
            
    return True, ""
