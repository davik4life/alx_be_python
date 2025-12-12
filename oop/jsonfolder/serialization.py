"""
    Create a Python function called process_json(data: dict, filename: str) -> dict that does the following:

Takes a dictionary (data) and a filename (filename) as input.
Serializes the dictionary to a JSON file with the given filename.
Deserializes the JSON file back into a dictionary.
Returns the deserialized dictionary.
"""

import json

def process_json(data: dict, filename: str) -> dict:
    # Serialize the dictionary to a JSON file
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

    # Deserialize the JSON file back into a dictionary
    with open(filename, 'r') as json_file:
        deserialized_data = json.load(json_file)
        return deserialized_data
#!/usr/bin/env python3

