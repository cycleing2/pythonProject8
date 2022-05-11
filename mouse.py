import pygame
from pygame import color

pygame.init()
width = 600
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("mouse")
image = pygame.image.load("微信图片_20220406155921.jpg")
rect = image.get_rect()
rect.topleft = (25, 25)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            rect.centerx = mouse_x
            rect.centery = mouse_y
        if event.type == pygame.MOUSEMOTION and event.buttons[0]==1:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            rect.centerx = mouse_x
            rect.centery = mouse_y
    display.fill((0, 0, 0))
    display.blit(image, rect)
    pygame.display.update()
pygame.quit()
