import json
from collections import defaultdict

# Load data from a JSON file
input_path = r'C:\Users\victo\Desktop\activities_services_mapping_clean\mapping_dates\herault_clean_sentence_case.json'
output_path = r'C:\Users\victo\Desktop\activities_services_mapping_clean\mapping_dates\titles_with_end_dates.json'

with open(input_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Collect all end_dates for each title
title_to_dates = defaultdict(set)

for entry in data:
    title = entry.get("title")
    end_date = entry.get("end_date")
    if title and end_date:
        title_to_dates[title].add(end_date)

# Convert sets to sorted lists
title_to_dates_sorted = {title: sorted(list(dates)) for title, dates in title_to_dates.items()}

# Write the result to a JSON file
with open(output_path, 'w', encoding='utf-8') as f_out:
    json.dump(title_to_dates_sorted, f_out, indent=4, ensure_ascii=False)

print(f"Output saved to: {output_path}")
