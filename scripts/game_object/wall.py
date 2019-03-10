# 標準ライブラリ
import os
import sys
import logging

# サードパーティライブラリ
import pygame
from pygame.locals import *

#
MODULE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
IMAGE_PATH = os.path.join(MODULE_PATH, "image")
SOUNDS_PATH = os.path.join(MODULE_PATH, "sounds")
SCRIPT_PATH = os.path.join(MODULE_PATH, "scripts")

# 自作モジュールの読み込み
sys.path.append(SCRIPT_PATH)
from load_resources import load_png_image

# ロガーの設定
logger = logging.getLogger(__file__)

# パラメータ
SCREEN_WIDTH = 1000  # 画面の横幅
SCREEN_HEIGHT = 500  # 画面の高さ


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png_image(os.path.join(IMAGE_PATH, "wall.png"))