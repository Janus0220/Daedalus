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

    image1 = pygame.image.load('tile.bmp') #タイルの画像
    image2 = pygame.image.load('black.bmp') #黒のコマ
    image3 = pygame.image.load('white.bmp') #白のコマ
    image1 = image1.convert()
    image2 = image2.convert()
    image3 = image3.convert()
    ckey2 = image2.get_at((0,0)) # カラーキーの取得
    ckey3 = image3.get_at((0,0))
    image2.set_colorkey(ckey2)
    image3.set_colorkey(ckey3)
    imagerect1 = image1.get_rect()
    imagerect2 = image2.get_rect()
    imagerect3 = image3.get_rect()

    pygame.mouse.set_visible(True) #マウスポインターの表示をオン
    whoturn = 0 # 誰の番かを示すフラグ
    # タイルで画面を埋める
    for i in range(0, WPOS+1, WDTH):
        for j in range(0, WPOS+1, WDTH):
            screen.blit(image1, imagerect1.move(i,j))
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event in pygame.event.get():
                return sys.exit(1)
            if (event.type == KEYDOWN and
                event.key == K_ESCAPE):
                return sys.exit(1) # ESCAPEキーが押されたら終了
            if event.type == MOUSEBUTTONDOWN:
                whoturn += 1
                xpos = int(pygame.mouse.get_pos()[0]/WDTH)
                ypos = int(pygame.mouse.get_pos()[1]/WDTH)
                if whoturn%2 == 0: #先手は黒コマを置く
                    screen.blit(image2, imagerect2.move(WDTH*xpos,WDTH*ypos))
                else: #後手は白コマを置く
                    screen.blit(image3, imagerect3.move(WDTH*xpos,WDTH*ypos))
                pygame.display.flip()