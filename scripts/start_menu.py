# 標準ライブラリ
import os
import sys
import logging

# サードパーティライブラリ
import pygame
from pygame.locals import *

# 自作モジュールの読み込み
from load_resources import load_png_image

# ロガーの設定
logger = logging.getLogger(__file__)

MODULE_PATH = os.path.dirname(os.path.dirname(__file__))
IMAGE_PATH = os.path.join(MODULE_PATH, "image")
SOUNDS_PATH = os.path.join(MODULE_PATH, "sounds")

# パラメータ
SCREEN_WIDTH = 1000  # 画面の横幅
SCREEN_HEIGHT = 500  # 画面の高さ


def init_start_menu():
    # スタートメニューの画面の作成
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Daedalus')

    # スタートメニュー画面の読み込み
    start_image, start_image_rect = load_png_image(os.path.join(IMAGE_PATH, "start_menu_tmp.png"))
    screen.blit(start_image, start_image_rect.move(0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event in pygame.event.get():
                logger.info("イベント{}が検知されました。".format(event.type))
            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                return sys.exit(1) # ESCAPEキーが押されたら終了
            if event.type == MOUSEBUTTONDOWN:
                pass
        pygame.display.flip()


if __name__ == '__main__':
    init_start_menu()