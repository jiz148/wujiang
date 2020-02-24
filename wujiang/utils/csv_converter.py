"""
csv_converter.py
converter for csv-to-json or csv-to-sqlite
**delete first lane of title after downloading the csv_file**
"""
import csv
import json
import os
import sqlite3

PY_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(PY_FILE_PATH)
DATA_PATH = os.path.join(PROJECT_PATH, 'data')
CSV_NAME = '武将yoo - 武将.csv'
JSON_NAME = 'wujiang_index.json'
SQLITE_NAME = 'wujiang_index.db'


class CsvConverter:

    def __init__(self, data_path=DATA_PATH, csv_name=CSV_NAME):
        self.data_path = data_path
        self.csv_name = csv_name
        self.csv_path = os.path.join(self.data_path, self.csv_name)
        self.csv_file = open(self.csv_path)

    def to_json(self, json_name=JSON_NAME):
        data = {}
        csv_reader = csv.DictReader(self.csv_file)
        for rows in csv_reader:
            name = rows['名称']  # name as a key
            data[name] = rows
        json_path = os.path.join(DATA_PATH, json_name)
        with open(json_path, 'w') as json_file:
            json_file.write(json.dumps(data, indent=4))

    def to_sqlite(self, sqlite_name=SQLITE_NAME):
        """
        Converter csv file to sqlite3 file
        """
        sqlite_path = os.path.join(DATA_PATH, sqlite_name)
        conn = sqlite3.connect(sqlite_path)

        cur = conn.cursor()

        cur.execute("CREATE TABLE wujiang("
                    "id INTEGER PRIMARY KEY,"
                    "level NUMERIC,"
                    "profession TEXT,"
                    "name TEXT,"
                    "attack NUMERIC,"
                    "defense NUMERIC,"
                    "speed NUMERIC,"
                    "ranging NUMERIC,"
                    "mag NUMERIC,"
                    "spells TEXT,"
                    "specs TEXT,"
                    "scepter TEXT)")

        reader = csv.reader(self.csv_file)

        for row in reader:
            cur.execute("INSERT INTO wujiang("
                        "level,"
                        "profession,"
                        "name, "
                        "attack,"
                        "defense, "
                        "speed,"
                        "ranging,"
                        "mag,"
                        "spells,"
                        "specs,"
                        "scepter) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", row)
        conn.commit()

    def close(self):
        """
        Closes the cvs file opened
        """
        self.csv_file.close()
