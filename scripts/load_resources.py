# 標準ライブラリ
import os
import sys
import logging

# サードパーティライブラリ
import pygame
from pygame.locals import *

# ロガーの設定
logger = logging.getLogger(__file__)

MODULE_PATH = os.path.dirname(os.path.dirname(__file__))
IMAGE_PATH = os.path.join(MODULE_PATH, "image")
SOUNDS_PATH = os.path.join(MODULE_PATH, "sounds")


#
def load_png_image(image_path):
    try:
        if os.path.isfile(image_path):
            image = pygame.image.load(image_path)
            logger.info("画像{}のロードに成功しました。".format(image_path))
        else:
            # テスト用のimageファイルをロードする
            image = pygame.image.load(os.path.join(os.path.dirname(image_path),
                                                   os.path.basename(image_path).split(".")[0], "_tmp",
                                                   os.path.basename(image_path).split(".")[1]))
            logger.warning("画像{}のロードに失敗しました。テスト用の画像を読み込みます。".format(image_path))
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error:
        logger.error('画像{}の読み込みに失敗しました。'.format(image_path))
        raise SystemExit
    return image, image.get_rect()
