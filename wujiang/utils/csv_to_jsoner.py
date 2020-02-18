"""
csv_to_jsoner.py
converter for csv-to-json for wujiang\
**delete first lane of title after downloading the csv_file**
"""
import csv
import json
import os

PY_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(PY_FILE_PATH)
DATA_PATH = os.path.join(PROJECT_PATH, 'data')
CSV_NAME = '武将yoo - 武将.csv'
JSON_NAME = 'wujiang_index.json'


class CsvToJsoner:

    def __init__(self, data_path=DATA_PATH, csv_name=CSV_NAME):
        self.data_path = data_path
        self.csv_name = csv_name
        self.csv_path = os.path.join(self.data_path, self.csv_name)
        self.data = {}
        with open(self.csv_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for rows in csv_reader:
                name = rows['名称']  # name as a key
                self.data[name] = rows

    def to_json(self, json_name=JSON_NAME):
        json_path = os.path.join(DATA_PATH, json_name)
        with open(json_path, 'w') as json_file:
            json_file.write(json.dumps(self.data, indent=4))
