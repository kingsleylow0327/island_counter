import sys
from pathlib import Path

# Validating Map
def map_validator(raw_array):
    ret_json = {}
    filtered_lines = []
    line_len = 0

    for item in raw_array:
        raw_line = item.strip()

        # Check for valid size (must be a x * y)
        if line_len == 0 and len(raw_line) != 0:
            line_len = len(raw_line)
        if len(raw_line) != line_len and raw_line != "":
            ret_json["status"] = "Error"
            ret_json["message"] = "Map shape of is not x*y"
            return ret_json

        # Check for empty lines
        if raw_line == "":
            ret_json["status"] = "Error"
            ret_json["message"] = "Map contained exessive empty lines"
            return ret_json

        # Check for characters
        if not all(ch in "01" for ch in raw_line):
            ret_json["status"] = "Error"
            ret_json["message"] = "Map contained characters other than '0' & '1'"
            return ret_json

        filtered_lines.append([c for c in raw_line])
    ret_json["status"] = "Ok"
    ret_json["message"] = filtered_lines
    return ret_json


# Main Counting Logic
def island_count(map):
    ret_json = {}
    if len(map) < 1:
        ret_json["status"] = "Error"
        ret_json["message"] = "Empty Map"
        return ret_json

    col = len(map)
    row = len(map[0])
    island_num = 0

    for y in range(col):
        for x in range(row):
            if map[y][x] == '1':
                walk(y, x, map)
                island_num += 1
    ret_json["status"] = "Ok"
    ret_json["message"] = str(island_num)
    return ret_json


# Map Walking logic
def walk(y, x, map):
    # Prevent walk out the map
    if y < 0 or y >= len(map) or x < 0 or x >= len(map[y]):
        return
    if map[y][x] == '1':
        map[y][x] = '0'  # Set 1 to 0 to prevent come back again
        walk(y-1, x, map)  # up
        walk(y+1, x, map)  # down
        walk(y, x-1, map)  # left
        walk(y, x+1, map)  # right


def main():
    ret_json = {}
    # Initialize Variable
    raw_array = []

    # Python script argument
    if len(sys.argv) <= 1:
        ret_json["status"] = "Error"
        ret_json["message"] = "Missing Text Path. Try: main.py <input>.txt"
        return ret_json

    # Check input path is existed and is txt file
    input_path = Path(sys.argv[1])
    if input_path.suffix != '.txt':
        ret_json["status"] = "Error"
        ret_json["message"] = f"'{input_path}' is not '.txt' file type"
        return ret_json

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
    json = map_validator(raw_array)

    if json["status"] == "Ok":
        json = island_count(json["message"])
    return json


if "__main__" == __name__:
    print(main())
