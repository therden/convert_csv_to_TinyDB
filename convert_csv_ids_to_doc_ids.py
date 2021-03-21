# This program converts a CSV file to a TinyDB database and prints the db file.
#
# It assumes that the first line of the CSV file contains field/column names.
#
# It further assumes that the CSV file includes ID numbers, which the
# user wants to preserve and assign as TinyDB's doc_ids (although this
# could create complications if you want to insert more records later
# _without_ using the Document class.)

import csv, json

from tinydb import TinyDB
from tinydb.table import Document

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
            id = tiny_record.pop("id")
            db.insert(Document(tiny_record, doc_id=id))

# for document in db.all():
#     print(f"doc_id: {document.doc_id}, name: {document['name']}")

json_object = open(output_file)
print(json.dumps(json.load(json_object), sort_keys=True, indent=2))
