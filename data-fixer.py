import json
import os

#Define Ranks
ranks = {
    "Hoodlum": 1,
    "Peddler": 2,
    "Hustler": 3,
}
ranklvls = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
}

# Set your file path as needed
file_path = os.path.join(os.path.dirname(__file__), 'data.json')

with open(file_path, 'r') as f:
    data = json.load(f)

for item in data:
    '''if "permutationLength" not in item:
        item["permutationLength"] = len(item["bestCombination"])
    if "maxRepetitions" in item:
        del item["maxRepetitions"]'''

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)