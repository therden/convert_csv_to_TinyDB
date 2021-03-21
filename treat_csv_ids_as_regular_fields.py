# This program converts a CSV file to a TinyDB database and prints the db file.
#
# It makes no attempt to handle csv record IDs as TinyDB doc_ids,
# allowing TinyDB to assign its own

import csv, json

from tinydb import TinyDB

source_file = "source.csv"
output_file = "output.json"

db = TinyDB(output_file)
db.truncate()  # empty the db file, in case it was previously populated

field_names = None
with open(source_file, encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for record in csv_reader:
        if not field_names:
            field_names = record
        else:
            tiny_record = dict(zip(field_names, record))
            db.insert(tiny_record)

json_object = open(output_file)
print(json.dumps(json.load(json_object), sort_keys=True, indent=2))
