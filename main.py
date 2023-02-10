import sys
from pathlib import Path


def map_validator(raw_array, input_path):
    filtered_lines = []
    line_len = 0

    for item in raw_array:
        raw_line = item.strip()

        # Check for valid size (must be a x * y)
        if line_len == 0 and len(raw_line) != 0:
            line_len = len(raw_line)
        if len(raw_line) != line_len and raw_line != "":
            print(f"Shape of '{input_path}' is not x*y")
            filtered_lines = []
            break

        # Check for empty lines
        if raw_line == "":
            print(f"'{input_path}' contained exessive empty lines")
            break

        # Check for characters
        if not all(ch in "01" for ch in raw_line):
            print(f"'{input_path}' contained characters other than '0' & '1'")
            break

        filtered_lines.append([c for c in raw_line])
    return filtered_lines


# Main Counting Logic
def island_count(map) -> int:
    if len(map) < 1:
        return "Empty Map"

    col = len(map)
    row = len(map[0])
    island_num = 0

    for y in range(col):
        for x in range(row):
            if map[y][x] == '1':
                walk(y, x, map)
                island_num += 1
    return island_num


# Map Walking logic
def walk(y, x, map):
    # Prevent walk out the map
    if y < 0 or y >= len(map) or x < 0 or x >= len(map[y]):
        return -1
    if map[y][x] == '1':
        map[y][x] = '0'  # Set 1 to 0 to prevent come back again
        walk(y-1, x, map)  # up
        walk(y+1, x, map)  # down
        walk(y, x-1, map)  # left
        walk(y, x+1, map)  # right


def main():
    # Initialize Variable
    raw_array = []

    # Python script argument
    if len(sys.argv) <= 1:
        print("Missing Text Path. Try: main.py <input>.txt")
        return "Error"

    # Check input path is existed and is txt file
    input_path = Path(sys.argv[1])
    if input_path.suffix != '.txt':
        print(f"'{input_path}' is not '.txt' file type")
        return "Error"

    if not input_path.is_file():
        print(f"'{input_path}' file not found")
        return "Error"

    # Read from txt file
    with open(input_path) as f:
        raw_array = f.readlines()

    # Check raw_array is not empty:
    if len(raw_array) < 1:
        print(f"'{input_path}' is an empty txt file")
        return "Error"

    # Checking 2D array
    map = map_validator(raw_array, input_path)

    island_number = island_count(map)
    return island_number


if "__main__" == __name__:
    print(main())
