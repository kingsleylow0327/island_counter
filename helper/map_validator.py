def map_validate(raw_array):
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