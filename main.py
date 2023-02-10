import re
import sys
from pathlib import Path

# Initialize Variable
raw_array = []
filtered_lines = []
line_len = 0

# Python script argument
if len(sys.argv) <=1 :
    print("Missing Text Path. Try: main.py <input>.txt")
    sys.exit()

# Check input path is existed and is txt file
input_path = Path(sys.argv[1])
if input_path.suffix != '.txt':
    print(f"'{input_path}' is not '.txt' file type")
    sys.exit()

if not input_path.is_file():
    print(f"'{input_path}' file not found")
    sys.exit()

# Read from txt file
with open (input_path) as f:
    raw_array = f.readlines()

# Check raw_array is not empty:
if len(raw_array) < 1:
    print(f"'{input_path}' is an empty txt file")
    sys.exit()

# Checking 2D array
for item in raw_array:
    raw_line = item.strip()

    # Check for valid size (must be a x * y)
    if line_len == 0 and len(raw_line) != 0:
        line_len = len(raw_line)
    if len(raw_line) != line_len and raw_line != "":
        print(f"Shape of '{input_path}' is not x*y")
        break
    
    # Check for empty lines
    if raw_line == "":
        print(f"'{input_path}' contained exessive empty lines")
        break
    
    # Check for characters
    if not all(ch in "01" for ch in raw_line):
        print(f"'{input_path}' contained characters other than '0' and '1'")
        break

    filtered_lines.append([c for c in raw_line])

# Main Counting Logic
def island_count(map) -> int:
    if len(map) < 1:
        return "This is an empty map"

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
        return
    if map[y][x] == '1':
        map[y][x] = '0' # Set 1 to 0 to prevent come back again
        walk(y-1, x, map) # up
        walk(y+1, x, map) # down
        walk(y, x-1, map) # left
        walk(y, x+1, map) # right
