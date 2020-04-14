"""
Wujiang.py
Wujiang class
"""
import json
import os
import random

from PIL import Image, ImageDraw, ImageFont

PY_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(PY_FILE_PATH)
DATA_PATH = os.path.join(PROJECT_PATH, 'data')
JSON_NAME = 'wujiang_index.json'
JSON_PATH = os.path.join(DATA_PATH, JSON_NAME)
IMAGE_PATH = os.path.join(DATA_PATH, 'cards')
FONT_PATH = os.path.join(PY_FILE_PATH, 'fonts')


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
        self.type = character.get('属性')
        self.race = character.get('种族')
        self.name = character.get('名称')
        self.attack = character.get('攻')
        self.defense = character.get('受')
        self.speed = character.get('速')
        self.ranging = character.get('范')
        self.mag = character.get('魔')
        self.spells = character.get('技能')
        self.specs = character.get('性质')
        # self.scepter = character.get('神杖加强')

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

    def to_card(self, card_path=IMAGE_PATH):
        """
        Generates a image to image path
        """
        img = Image.new('RGB', (450, 650), color=(243, 210, 119))
        draw = ImageDraw.Draw(img)
        regular_font_path = os.path.join(FONT_PATH, 'chinese.msyh.ttf')

        draw.text((10, 10), self.name, font=ImageFont.truetype(regular_font_path, 30), fill='black')
        draw.text((410, 10), str(self.level), font=ImageFont.truetype(regular_font_path, 30), fill='black')
        draw.text((10, 50), str(self.type), font=ImageFont.truetype(regular_font_path, 15), fill='black')
        draw.text((50, 50), str(self.race), font=ImageFont.truetype(regular_font_path, 15), fill='black')
        draw.text((400, 40), str(self.profession), font=ImageFont.truetype(regular_font_path, 20), fill='black')
        draw.text((10, 80), '攻: ' + self.attack, font=ImageFont.truetype(regular_font_path, 20), fill='black')
        draw.text((100, 80), '受: ' + self.defense, font=ImageFont.truetype(regular_font_path, 20), fill='black')
        draw.text((190, 80), '速: ' + self.speed, font=ImageFont.truetype(regular_font_path, 20), fill='black')
        draw.text((280, 80), '范: ' + self.ranging, font=ImageFont.truetype(regular_font_path, 20), fill='black')
        draw.text((370, 80), '魔: ' + self.mag, font=ImageFont.truetype(regular_font_path, 20), fill='black')
        draw.text((10, 110), '技能:', font=ImageFont.truetype(regular_font_path, 20), fill='black')
        draw.text((10, 135), self._auto_new_line(self.spells, 31), font=ImageFont.truetype(regular_font_path, 14), fill='black')
        draw.text((10, 370), '性质:', font=ImageFont.truetype(regular_font_path, 20), fill='black')
        draw.text((10, 400), self._auto_new_line(self.specs, 31), font=ImageFont.truetype(regular_font_path, 14), fill='black')
        card_name = self.name + '.png'
        card_path = os.path.join(card_path, card_name)

        img.save(card_path)

    def _auto_new_line(self, string, width):
        """
        Given a string, change auto change to string with new line
        """
        count = 0
        for i in range(len(string)):
            count += 1
            if count > width:
                string = string[0:i] + '\n' + string[i:]
                i += 1
                count = 0
        return string
