# 標準ライブラリ
import os
import sys
import logging

# サードパーティライブラリ
import pygame
from pygame.locals import *

# 自作モジュールの読み込み
from load_resources import load_png_image
from game_object.start_menu_object import StartGameMenu, SettingGameMenu, ExitGameMenu

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
    # マウスを見えるようにする。
    pygame.mouse.set_visible(True)

    # スタートメニューのメニュー画面の表示
    start_menu = StartGameMenu()
    setting_menu = SettingGameMenu()
    exit_menu = ExitGameMenu()
    allsprites = pygame.sprite.RenderPlain((start_menu, setting_menu, exit_menu))
    allsprites.draw(screen)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            start_menu.move_on_mouse(pos[0], pos[1])
            setting_menu.move_on_mouse(pos[0], pos[1])
            exit_menu.move_on_mouse(pos[0], pos[1])
            if event in pygame.event.get():
                logger.info("イベント{}が検知されました。".format(event.type))

            if (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == QUIT):
                return sys.exit(1)  # ESCAPEキーが押されたら終

            if (event.type == MOUSEBUTTONDOWN):
                start_menu.click(pos[0], pos[1])
                setting_menu.click(pos[0], pos[1])
                exit_menu.click(pos[0], pos[1])

            allsprites.update()
            allsprites.draw(screen)
            pygame.display.flip()

if __name__ == '__main__':
    init_start_menu()