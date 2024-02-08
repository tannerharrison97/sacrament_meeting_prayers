import csv
from datetime import datetime
import json
import random

def get_week_number():
    now = datetime.now()
    iso_calendar = now.isocalendar()
    week_number = iso_calendar[1]
    return week_number

exclude_list = set()

with open('exclude-list.txt', 'r') as txtfile:
    for line in txtfile.readlines():
        exclude_list.add(line[:-1])

# Load CSV data into a list of dictionaries
contacts = []
with open('list-of-people.tsv', 'r') as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter='\t')
    for row in reader:
        if row["Preferred Name"] not in exclude_list:
            row["firstName"] = row["Preferred Name"].split(',')[1].split()[0]
            row["lastName"] = row["Preferred Name"].split(',')[0]
            contacts.append(row)

# Shuffle the contacts list for random order
random.shuffle(contacts)
number_of_weeks = len(contacts) // 4

current_week_number = get_week_number()

# Assign pairs to weeks
result = {}
for i in range(number_of_weeks):
    prayers = {
        "opening_prayer": {
            "first": contacts[i],
            "second": contacts[i + number_of_weeks],
        },
        "closing_paryer": {
            "first": contacts[i + 2 * number_of_weeks],
            "second": contacts[i + 3 * number_of_weeks],
        }
    }
    week_key = f'{i + current_week_number:02d}'  # Zero-padded week number
    result[week_key] = prayers

# Now write the JSON object to a file
with open('schedule.json', 'w') as jsonfile:
    json.dump(result, jsonfile, indent=4)

print("JSON data has been written to contact_pairs.json")