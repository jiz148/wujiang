"""
main.py
"""
import json


from utils.csv_converter import CsvConverter
from common.wujiang import Wujiang


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


if __name__ == "__main__":
    to_sqlite()
