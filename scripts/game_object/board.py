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


class Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png_image(os.path.join(IMAGE_PATH, "tile.png"))
        self.tile_image, self.tile_rect = load_png_image(os.path.join(IMAGE_PATH, "tile.png"))
        self.groove_image, self.groove_rect = load_png_image(os.path.join(IMAGE_PATH, "groove.png"))
        self.rect.x, self.rect.y = (300, 50)
        self.tile = [{j: None for j in range(i+1) if not j % 2} for i in range(20, 400, 20)]
        self.groove = [{j: None for j in range(i) if j % 2} for i in range(20, 400, 20)]

    def init_board(self, screen):
        for i in range(0, 21):
            for j in range(0, 21):
                if (j%2) :
                    screen.blit(self.groove_image, self.groove_rect.move(300+(21*i), 50+(21*j)))
                elif (i%2):
                    screen.blit(self.groove_image, self.groove_rect.move(300 + (21 * i), 50 + (21 * j)))
                else:
                    screen.blit(self.tile_image, self.tile_rect.move(300 + (21*i), 50+(21*j)))

    def update(self):
        pass

