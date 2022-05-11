import pygame

pygame.init()
width = 600
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("continuous")
FPS = 90
clock = pygame.time.Clock()
velocity = 5
image = pygame.image.load("微信图片_20220406155921.jpg")
rect = image.get_rect()
rect.center = (width // 2, height // 2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    print(keys)
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and rect.left > 0:
        rect.x -= velocity
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and rect.right < width:
        rect.x += velocity
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and rect.top > 0:
        rect.y -= velocity
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and rect.bottom < height:
        rect.y += velocity
    display.fill((0, 0, 0))
    display.blit(image, rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
