import csv
import json
import sys

# Load the contents of a CSV file
# Handle file and csv format exceptions
input_filename = 'iris.csv'
output_filename = 'iris-summary.json'
data = []
try:
  with open(input_filename) as f:
    csv_data = csv.DictReader(f)
    for rec in csv_data:
      data.append(rec)

except IOError:
  print('Failed to read file.')

if not data:
  raise ValueError('No data found.')

# Process or filter the data as necessary
print('Type of data: {}'.format(type(data)))
species = set()
counts = {}
for s in data:
  species.add(s['species'])
  if s['species'] in counts:
    counts[s['species']] += 1
  else:
    counts[s['species']] = 1

result = {
  'species' : list(species),
  'counts' : counts
}

# Save the resulting data to a file in JSON format
try:
  with open(output_filename, 'w') as f:
    json.dump(result, f, indent=2)
except IOError:
  print('Failed to write JSON file.')
except:
  print(sys.exc_info())