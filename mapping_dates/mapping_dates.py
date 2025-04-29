import json
from collections import defaultdict

# Load data from a JSON file
with open('events.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Collect all start_dates for each title
title_to_dates = defaultdict(set)

for entry in data:
    title = entry["title"]
    start_date = entry["start_date"]
    title_to_dates[title].add(start_date)

# Convert sets to sorted lists
title_to_dates_sorted = {title: sorted(list(dates)) for title, dates in title_to_dates.items()}

# Convert to JSON string and print
result_json = json.dumps(title_to_dates_sorted, indent=4, ensure_ascii=False)
print(result_json)
