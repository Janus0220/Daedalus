# 標準ライブラリ
import os
import logging
import sys

# サードパーティライブラリ
from PIL import Image, ImageFont, ImageDraw

# ロガーの設置
logger = logging.getLogger(__name__)

MODULE_PATH = os.path.dirname(os.path.dirname(__file__))
FONT_PATH = os.path.join(MODULE_PATH, "fonts")


def make_image_for_start_menu(image_name):
    width = 1000
    height = 500
    im = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    try:
        font = ImageFont.truetype(os.path.join(FONT_PATH, "ipamp.ttf"), 60)
    except OSError as e:
        logger.error("{}を読み込めませんでした。".format(os.path.join(FONT_PATH, "ipamp.ttf")))
        raise e
    draw.multiline_text((width * 0.32, height * 0.1), "DAEDALUS", fill=(255, 255, 255), font=font)
    draw.rectangle((250, 200, 750, 400), fill=(0, 0, 0), outline=(255, 255, 255), width=5)
    im.show()
    im.save(os.path.join(os.getcwd(), image_name))


if __name__ == '__main__':
    image_name = "start_menu_tmp.png"
    make_image_for_start_menu(image_name)
