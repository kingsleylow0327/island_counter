from helper.island_counter import island_count
from helper.map_validator import map_validate
from pathlib import Path


def main():
    ret_json = {}
    # Initialize Variable
    raw_array = []
    input_path = Path("./input.txt")

    if not input_path.is_file():
        ret_json["status"] = "Error"
        ret_json["message"] = f"'{input_path}' file not found"
        return ret_json

    # Read from txt file
    with open(input_path) as f:
        raw_array = f.readlines()

    # Check raw_array is not empty:
    if len(raw_array) < 1:
        ret_json["status"] = "Error"
        ret_json["message"] = f"'{input_path}' is an empty txt file"
        return ret_json

    # Checking 2D array
    json = map_validate(raw_array)

    if json["status"] == "Ok":
        json = island_count(json["message"])
    return json


if "__main__" == __name__:
    print(main())
