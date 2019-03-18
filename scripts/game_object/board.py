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
from .wall import Wall
from .player import Player


# ロガーの設定
logger = logging.getLogger(__file__)

# パラメータ
SCREEN_WIDTH = 1000  # 画面の横幅
SCREEN_HEIGHT = 500  # 画面の高さ


class Board:
    def __init__(self):
        self.tile_image, self.tile_rect = load_png_image(os.path.join(IMAGE_PATH, "tile.png"))
        self.groove_image, self.groove_rect = load_png_image(os.path.join(IMAGE_PATH, "groove.png"))
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

    def blit_board(self, screen):
        """"""
        pass

    def update_board_info(self, instance, position, ex_position):
        if isinstance(instance, Wall) and isinstance(int, position):
            self.tile[position] = 1
        elif isinstance(instance, Player):
            self.tile[position] = 2
            self.tile[ex_position] = 0
        else:
            logger.warning("")
            raise ValueError("")

    def show_choosable_action(self, instance, pos):
        """"""
        pass

    def det_action(self, instance, pos):
        """"""
        pass

