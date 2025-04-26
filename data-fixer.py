import json
import os

# Set your file path as needed
file_path = os.path.join(os.path.dirname(__file__), 'data.json')

with open(file_path, 'r') as f:
    data = json.load(f)

for item in data:
    if "permutationLength" not in item:
        item["permutationLength"] = len(item["bestCombination"])
    if "maxRepetitions" in item:
        del item["maxRepetitions"]

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)