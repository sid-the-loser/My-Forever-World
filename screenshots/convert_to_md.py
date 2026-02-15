import json
import os

import generate_notes

print("Converting all the image data into markdown...")

NOTES_PATH = "notes.json"

OUTPUT_PATH = "screenshots.md"

sorted_dir_list = sorted(os.listdir(), reverse=True)

notes_data = {}

md_data = ""

with open(NOTES_PATH) as f:
        notes_data = json.load(f)

for item in sorted_dir_list:
    if os.path.isfile(item) and item.endswith(".png"):
        date_n_time = item[:-4].split("_")

        _note = "Not written!"

        if item in notes_data:
             _note = notes_data[item]

        md_data += f">![{item}]({item})\n>\n>Date (YYYY-MM-DD): {date_n_time[0]}\n>\n>Time (HH.MM.SS): {date_n_time[1]}\n>\n>Notes: {_note}\n\n"

with open(OUTPUT_PATH, "w") as f:
    f.write(md_data)

print("Done!")