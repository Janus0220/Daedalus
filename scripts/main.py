# 標準ライブラリ
import os
import sys
import logging

# サードパーティライブラリ
import pygame
from pygame.locals import *

# ロガーの設定
logger = logging.getLogger(__file__)
logger.setLevel(Warning)

MODULE_PATH = os.path.dirname(os.path.dirname(__file__))
IMAGE_PATH = os.path.join(MODULE_PATH, "image")
SOUNDS_PATH = os.path.join(MODULE_PATH, "sounds")

# パラメータ
SCREEN_WIDTH = 1000  # 画面の横幅
SCREEN_HEIGHT = 500  # 画面の高さ


def main():
    # スタートメニューの作成
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Daedalus')

