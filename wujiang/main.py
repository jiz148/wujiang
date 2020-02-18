"""
main.py
"""
import json


from utils.csv_to_jsoner import CsvToJsoner
from common.wujiang import Wujiang


def dump_json():
    """
    Dumps csv to json
    """
    csv_to_jsoner = CsvToJsoner()
    csv_to_jsoner.to_json()


def get_character():
    """
    gets a character
    """
    print('Randomizing a Wujiang!')
    wujiang = Wujiang()
    wujiang.random()
    for attr, value in wujiang.__dict__.items():
        print(attr, ': ', value)


if __name__ == "__main__":
    get_character()
