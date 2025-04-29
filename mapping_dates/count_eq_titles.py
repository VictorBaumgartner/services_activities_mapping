import json
from collections import Counter

# Paths for input and output
input_path = r'C:\Users\victo\Desktop\activities_services_mapping_clean\mapping_dates\herault_clean_sentence_case.json'
output_path = r'C:\Users\victo\Desktop\activities_services_mapping_clean\mapping_dates\title_frequencies_detailed.json'

# Load data from input JSON
with open(input_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Count occurrences of each title
title_counter = Counter()

for entry in data:
    title = entry.get("title")
    if title:
        title_counter[title] += 1

# Convert to the desired format: { "title": { "count": X } }
title_freq_detailed = {title: {"count": count} for title, count in title_counter.items()}

# Save result to output JSON
with open(output_path, 'w', encoding='utf-8') as out_file:
    json.dump(title_freq_detailed, out_file, indent=4, ensure_ascii=False)

print(f"Detailed title frequencies saved to: {output_path}")
