"""
Wujiang.py
Wujiang class
"""
import json
import os
import random


PY_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(PY_FILE_PATH)
DATA_PATH = os.path.join(PROJECT_PATH, 'data')
JSON_NAME = 'wujiang_index.json'
JSON_PATH = os.path.join(DATA_PATH, JSON_NAME)


class Wujiang:

    def __init__(self, name: str = None):
        self.name = name
        if self.name:
            self.construct(self.name)

    def construct(self, name: str):
        """
        construct wujiang with name
        @param name: <str> name of wujiang
        """
        with open(JSON_PATH, 'r') as json_file:
            data = json.loads(json_file.read())

        character = data.get(name)
        self.level = int(character.get('等级'))
        self.profession = character.get('职业')
        self.name = character.get('名称')
        self.attack = float(character.get('攻'))
        self.defense = float(character.get('受'))
        self.speed = float(character.get('速'))
        self.ranging = float(character.get('范'))
        self.mag = float(character.get('魔'))
        self.spells = character.get('技能')
        self.specs = character.get('性质')
        self.scepter = character.get('神杖加强')

    def random(self):
        """
        Randoms a character and reconstruct Wujiang
        """
        with open(JSON_PATH, 'r') as json_file:
            data = json.loads(json_file.read())

        key_list = list(data.keys())
        random_id = random.randint(0, len(key_list) - 1)
        random_name = key_list[random_id]
        self.construct(random_name)
