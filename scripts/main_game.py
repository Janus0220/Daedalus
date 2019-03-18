# 標準ライブラリ
import os
import sys
import logging

# サードパーティライブラリ
import numpy as np
import pygame
from pygame.locals import *

# 自作モジュールの読み込み
from load_resources import load_png_image
from game_object.board import Board
from game_object.player import Player
from game_object.wall import Wall

# ロガーの設定
logger = logging.getLogger(__file__)

MODULE_PATH = os.path.dirname(os.path.dirname(__file__))
IMAGE_PATH = os.path.join(MODULE_PATH, "image")
SOUNDS_PATH = os.path.join(MODULE_PATH, "sounds")

# パラメータ
SCREEN_WIDTH = 1000  # 画面の横幅
SCREEN_HEIGHT = 500  # 画面の高さ


def init_main_game():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Daedalus')

    # ゲーム画面の読み込み
    game_image, game_image_rect = load_png_image(os.path.join(IMAGE_PATH, "main_game_temp.png"))
    screen.blit(game_image, game_image_rect.move(0, 0))

    # ゲームオブジェクトの開始
    board = Board()
    board.init_board(screen)
    """
    allsprites = pygame.sprite.RenderPlain()
    allsprites.draw(screen)
    """
    pygame.display.flip()

    # ゲーム情報の初期化
    player1_pos = 6
    player2_pos = 20*21 + 6
    #player1 = Player(player1_pos, "red")
    #player2 = Player(player2_pos, "blue")
    """
    構造
    player1の描画
    player2の描画
    
    WallかPlayerスイッチの選択
        WallならばWallの位置を選択する
        Boardインスタンスがその場所にWallがおけるか判定する。
            Boardインスタンスの情報を更新する。 / 出来なければ、エラーを表示する。
        Playerインスタンスの情報を更新する。
        
        PlayerならばPlayerの位置の候補を選択する
        以後同じ
        
    
    
    """

    # メインループ
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == QUIT):
                return sys.exit(1)


        #allsprites.update()
        #allsprites.draw(screen)
        pygame.display.flip()