import json
import os
from slugify import slugify

# Load JSONL file
jsonl_file = '/home/iguana/WebstormProjects/fm-cheatsheet/assets/categories.jsonl'

# Create directories and index.md files
with open(jsonl_file, 'r') as f:
    for line in f:
        category = json.loads(line)
        category_name = category['title']
        slugified_category_name = slugify(category_name)
        category_dir = f'/home/iguana/WebstormProjects/fm-cheatsheet/content/english/foundation-model-resources/{slugified_category_name}'
        index_md_path = os.path.join(category_dir, 'index.md')

        # Create directory
        os.makedirs(category_dir, exist_ok=True)

        # Write to index.md file
        with open(index_md_path, 'w') as md_file:
            md_file.write('---\n')
            md_file.write(f'title: "{category_name}"\n')
            md_file.write(f'short_name: "{category_name}"\n')
            md_file.write('type: "tools-directory"\n')
            md_file.write('nofollow: true\n')
            md_file.write('date: \'2023-12-26\'\n')  # You can modify the date as needed
            md_file.write(f'description: "{category_name}"\n')
            md_file.write('highlight: true\n')  # You can modify this value as needed
            md_file.write('image: machine-learning-benchmark.jpeg\n')  # You can modify the image path as needed
            md_file.write(f'details: "{category[category_name]}"\n')  # Assuming details is a key in the category dictionary
            md_file.write('---\n')
