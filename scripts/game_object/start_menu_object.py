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


class StartGameMenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png_image(os.path.join(IMAGE_PATH, "start_menu_band_temp.png"))
        self.image_on_mouse, self.rect_on_mouse = load_png_image(os.path.join(IMAGE_PATH,
                                                                              "start_menu_band_on_mouse_temp.png"))
        self.rect.center = (SCREEN_WIDTH/2, 250)
        self.rect_on_mouse.center = (SCREEN_WIDTH / 2, 250)
        self.original_image, self.original_rect = self.image, self.rect
        self.clicked = 0
        self.on_mouse = 0

    def update(self):
        self.change_image_on_mouse()
        if self.clicked:
            # TODO ゲームの開始を宣言する。
            pass

    def click(self, click_x, click_y):
        hitbox = self.rect
        self.clicked = hitbox.collidepoint(click_x, click_y)

    def change_image_on_mouse(self):
        if self.on_mouse:
            self.image, self.rect = self.image_on_mouse, self.rect_on_mouse
        else:
            self.image, self.rect = self.original_image, self.original_rect

    def move_on_mouse(self, click_x, click_y):
        hitbox = self.rect
        self.on_mouse = hitbox.collidepoint(click_x, click_y)


class SettingGameMenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png_image(os.path.join(IMAGE_PATH, "setting_menu_band_temp.png"))
        self.image_on_mouse, self.rect_on_mouse = load_png_image(os.path.join(IMAGE_PATH,
                                                                              "setting_menu_band_on_mouse_temp.png"))
        self.rect.center = (SCREEN_WIDTH/2, 300)
        self.rect_on_mouse.center = (SCREEN_WIDTH / 2, 300)
        self.original_image, self.original_rect = self.image, self.rect
        self.clicked = 0
        self.on_mouse = 0

    def update(self):
        self.change_image_on_mouse()
        if self.clicked:
            # TODO ゲームの設定画面を開く。
            pass

    def click(self, click_x, click_y):
        hitbox = self.rect
        self.clicked = hitbox.collidepoint(click_x, click_y)

    def change_image_on_mouse(self):
        if self.on_mouse:
            self.image, self.rect = self.image_on_mouse, self.rect_on_mouse
        else:
            self.image, self.rect = self.original_image, self.original_rect

    def move_on_mouse(self, click_x, click_y):
        hitbox = self.rect
        self.on_mouse = hitbox.collidepoint(click_x, click_y)


class ExitGameMenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png_image(os.path.join(IMAGE_PATH, "finish_menu_band_temp.png"))
        self.image_on_mouse, self.rect_on_mouse = load_png_image(os.path.join(IMAGE_PATH,
                                                                              "finish_menu_band_on_mouse_temp.png"))
        self.rect.center = (SCREEN_WIDTH/2, 350)
        self.rect_on_mouse.center = (SCREEN_WIDTH/2, 350)
        self.original_image, self.original_rect = self.image, self.rect
        self.clicked = 0
        self.on_mouse = 0

    def update(self):
        self.change_image_on_mouse()
        if self.clicked:
            sys.exit(1)

    def click(self, click_x, click_y):
        hitbox = self.rect
        self.clicked = hitbox.collidepoint(click_x, click_y)

    def change_image_on_mouse(self):
        if self.on_mouse:
            self.image, self.rect = self.image_on_mouse, self.rect_on_mouse
        else:
            self.image, self.rect = self.original_image, self.original_rect

    def move_on_mouse(self, click_x, click_y):
        hitbox = self.rect
        self.on_mouse = hitbox.collidepoint(click_x, click_y)
