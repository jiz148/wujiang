"""
main.py
"""
import json
import os


from utils.csv_converter import CsvConverter
from common.wujiang import Wujiang

PY_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(PY_FILE_PATH, 'data')
JSON_NAME = 'wujiang_index.json'
JSON_PATH = os.path.join(DATA_PATH, JSON_NAME)


def dump_json():
    """
    Dumps csv to json
    """
    csv_converter = CsvConverter()
    csv_converter.to_json()
    csv_converter.close()


def get_character():
    """
    gets a character
    """
    print('Randomizing a Wujiang!')
    wujiang = Wujiang()
    wujiang.random()
    for attr, value in wujiang.__dict__.items():
        print(attr, ': ', value)


def to_sqlite():
    """
    Dumps csv to sqlite
    """
    csv_conveter = CsvConverter()
    csv_conveter.to_sqlite()
    csv_conveter.close()


def print_imgs():
    """
    Print a image
    """
    with open(JSON_PATH, 'r') as fp:
        data = json.loads(fp.read())
    for w in data:
        wujiang = Wujiang(w)
        wujiang.to_card()


if __name__ == "__main__":
    dump_json()
    to_sqlite()
    print_imgs()
