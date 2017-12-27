import os
import sys
import json
# import json.tool
# import pprint


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            return json.load(file)
    else:
        print("File path not correct")
        sys.exit(1)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        json_file_path = sys.argv[-1]
        json_raw_data = load_data(json_file_path)
        pretty_print_json(json_raw_data)

    else:
        print("Please, specify the path to the file (json)")
        sys.exit(1)
