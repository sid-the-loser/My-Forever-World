import os

sorted_dir_list = sorted(os.listdir())

md_data = ""

for item in sorted_dir_list:
    if os.path.isfile(item) and item.endswith(".png"):
        md_data += f"![{item}]({item} =100x)\n"

with open("screenshots.md", "w") as f:
    f.write(md_data)