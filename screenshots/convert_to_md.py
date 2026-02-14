import os

sorted_dir_list = sorted(os.listdir())

md_data = ""

for item in sorted_dir_list:
    if os.path.isfile(item) and item.endswith(".png"):
        date_n_time = item[:-4].split("_")

        md_data += f">![{item}]({item})\n>\n>Filename: {item}\n>\n>Date: {date_n_time[0]}\n>\n>Time: {date_n_time[1]}\n\n"

with open("screenshots.md", "w") as f:
    f.write(md_data)