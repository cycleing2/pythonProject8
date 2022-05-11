import pygame

pygame.init()
width = 800
height = 800
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("cpdd")
velocity = 100
image = pygame.image.load("微信图片_20220406155921.jpg")
rect = image.get_rect()
rect.centerx = width // 2
rect.bottom = height
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.x -= velocity
            if event.key == pygame.K_RIGHT:
                rect.x += velocity
            if event.key == pygame.K_UP:
                rect.y -= velocity
            if event.key == pygame.K_DOWN:
                rect.y += velocity
    display.fill((0, 0, 0))
    display.blit(image, rect)
    pygame.display.update()
pygame.quit()
