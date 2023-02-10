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