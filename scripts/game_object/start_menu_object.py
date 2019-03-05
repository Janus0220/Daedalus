# 標準ライブラリ
import os
import sys
import logging

# サードパーティライブラリ
import pygame
from pygame.locals import *

# 自作モジュールの読み込み
from .load_resources import load_png_image
#from game_object import menu

# ロガーの設定
logger = logging.getLogger(__file__)

MODULE_PATH = os.path.dirname(os.path.dirname(__file__))
IMAGE_PATH = os.path.join(MODULE_PATH, "image")
SOUNDS_PATH = os.path.join(MODULE_PATH, "sounds")


class StartMenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png_image(os.path.join(IMAGE_PATH, "start_menu_band_temp.png"))
        self.click = 0