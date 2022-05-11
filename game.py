import os.path

import pygame
import sys
from pygame.locals import *
pygame.init()
# 定义窗口样式
width = 600
height = 600
display_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("hello word")
# 颜色的设置
yellow = (255, 255, 0)
red = (255, 0, 0)
white = (0, 0, 55)
# 窗口设置背景颜色
display_surface.fill(yellow)
# pygame.draw.line(display_surface, red, (0, 0), (100, 100), 5)
# pygame.draw.circle(display_surface,white,(width//2,height//2),200,6)
# pygame.draw.rect(display_surface,white,(500,10,50,100))
# 窗口中插入图片
# left = pygame.image.load(os.path.join('left.png'))
# left_rect = left.get_rect()
# left_rect.topleft(0, 0)
# right = pygame.image.load(os.path.join('left.png'))
# right_rect = left.get_rect()
# right_rect.topright(width, 0)
a=pygame.mixer.Sound("孤勇者 - 陈奕迅.mp3")

a.play()
pygame.time.delay(2000)

a.set_volume(.1)
a.play()
pygame.mixer.music.load('Letting Go - 蔡健雅.mp3')
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.stop()
# 退出窗口
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    # display_surface.blit(left, left_rect)
    # display_surface.blit(right, right_rect)
    pygame.display.update()
# 结束游戏
pygame.quit()
