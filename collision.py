import pygame,random

pygame.init()
width = 600
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("coll")
velocity = 5
clock = pygame.time.Clock()
image = pygame.image.load("微信图片_20220406155921.jpg")
rect = image.get_rect()
rect.topleft = (25, 25)
image_2 = pygame.image.load("preview.jpg")
rect_2 = image_2.get_rect()
rect_2.center = (width // 2, height // 2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect.left > 0:
        rect.x -= velocity
    if keys[pygame.K_RIGHT] and rect.right < width:
        rect.x += velocity
    if keys[pygame.K_UP] and rect.top > 0:
        rect.y -= velocity
    if keys[pygame.K_DOWN] and rect.bottom < height:
        rect.y += velocity
    if rect.colliderect(rect_2):
        print("hit")
        rect_2.x=random.randint(0,width-10)
        rect_2.y=random.randint(0,height-10)
    display.fill((0, 0, 0))
    pygame.draw.rect(display, (0, 255, 0), rect, 80)
    pygame.draw.rect(display, (255, 255, 0), rect_2, 80)
    display.blit(image, rect)
    display.blit(image_2, rect_2)
    pygame.display.update()
    clock.tick(90)
pygame.quit()
