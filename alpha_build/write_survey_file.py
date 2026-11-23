import json
import os
import tempfile


def write_survey_file(filename, data):
    """Write coordinate data atomically as formatted UTF-8 JSON."""
    destination_directory = os.path.dirname(os.path.abspath(filename))
    temporary_filename = None

    try:
        os.makedirs(destination_directory, exist_ok=True)

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=destination_directory,
            prefix=".surveytool-",
            suffix=".tmp",
            delete=False,
        ) as survey_file:
            temporary_filename = survey_file.name
            json.dump(data, survey_file, indent=2)
            survey_file.write("\n")
            survey_file.flush()

            try:
                os.fsync(survey_file.fileno())
            except OSError:
                pass

        os.replace(temporary_filename, filename)
        temporary_filename = None
    except PermissionError:
        print(f"Permission denied while writing: {filename}")
        return False
    except OSError as error:
        print(f"Could not write {filename}: {error}")
        return False
    finally:
        if temporary_filename is not None:
            try:
                os.unlink(temporary_filename)
            except OSError:
                pass

    return True
