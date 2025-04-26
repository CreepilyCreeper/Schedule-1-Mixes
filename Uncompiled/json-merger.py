import json
import glob

read_files = glob.glob("*.json")
output_list = []

for f in read_files:
    with open(f, "rb") as infile:
        output_list.append(json.load(infile))
'''
all_items = []
for json_file in output_list:
    all_items += json_file['items']
'''
all_items = output_list

textfile_merged = open('data.json', 'w')
json.dump(all_items, textfile_merged, default = lambda x: x.__dict__)
textfile_merged.close()
