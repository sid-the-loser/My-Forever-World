import os
import json

print("Generating notes...")

OUTPUT_PATH = "notes.json"

dir_list = os.listdir()

notes_data = {}

if not os.path.isfile(OUTPUT_PATH):
    with open(OUTPUT_PATH, "w") as f:
        f.write("{}")

else:
    with open(OUTPUT_PATH) as f:
        notes_data = json.load(f)

for item in dir_list:
    if os.path.isfile(item) and item.endswith(".png") and (item not in notes_data):
        notes_data[item] = "To be added..."

with open(OUTPUT_PATH, "w") as f:
    json.dump(notes_data, f, indent=0, sort_keys=True)

print("Done!")