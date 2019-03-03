# 標準ライブラリ
import os
import sys

# サードパーティライブラリ
from PIL import Image, ImageFont, ImageDraw

MODULE_PATH = os.path.dirname(os.path.dirname(__file__))
FONT_PATH = os.path.join(MODULE_PATH, "font")


def make_image_for_start_menu(image_name):
    width = 1000
    height = 500
    im = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(os.path.join(FONT_PATH, "ipamp.ttf"), 60)
    draw.multiline_text((width * 0.32, height * 0.1), "DAEDALUS", fill=(255, 255, 255), font=font)
    im.save(os.path.join(os.getcwd(), image_name))


if __name__ == '__main__':
    image_name = "start_menu_tmp.png"
    make_image_for_start_menu(image_name)
