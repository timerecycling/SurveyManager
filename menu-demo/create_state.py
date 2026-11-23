def create_state():
    """Create the shared state used by every survey operation."""
    state = {
        "loaded_filename": None,
        "memory": {},
        "file_data": {},
    }

    return state
