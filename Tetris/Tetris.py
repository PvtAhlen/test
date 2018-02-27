

#coding: utf-8
import pygame
from pygame.locals import *
import sys

def main():
    (w, h) = (400, 400) #画面サイズ
    (x, y) = (w//2, h//2)
    pygame.init()   #Pygameの初期化
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Tetris")    #タイトルバーに表示する文字

    while(1):
        pygame.display.update() #画面更新
        pygame.time.wait(30) #更新時間間隔
        screen.fill((0, 20, 0, 0))
        #円の中心座標が画面の範囲外にある場合
        if x < 0:
            x = 0
        if x > w:
            x = w
        if y < 0:
            y = 0
        if y > h:
            y = h
        pygame.mouse.set_visible(False)
        #円を描画
        pygame.draw.circle(screen, (0, 200, 0), (x, y), 5, 0)
        (x, y) = pygame.mouse.get_pos()

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT: #閉じるボタンが押されたら終了
                pygame.quit() #Pygameの終了(画面閉じられる)
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                #矢印キーなら円の中心座標を矢印の方向に移動
                if event.key == K_LEFT:
                    x -= 10
                if event.key == K_RIGHT:
                    x += 10
                if event.key == K_UP:
                    y -= 10
                if event.key == K_DOWN:
                    y += 10
if __name__ == "__main__":
    main()



