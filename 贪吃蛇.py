import pygame, random

pygame.init()
width = 600
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()
# 游戏参数
snake_size = 20
head_x = width // 2
head_y = height // 2 + 100
snake_dx = 0
snake_dy = 0
score = 0
# 颜色
green = (0, 255, 0)
darkgreen = (10, 50, 10)
red = (255, 0, 0)
darkred = (150, 0, 0)
white = (255, 255, 255)
# 字体样式
font = pygame.font.SysFont("gabriola", 48)
# 文本
tile_text = font.render("--snake--", True, green, darkred)
tile_rect = tile_text.get_rect()
tile_rect.center = (width // 2, height // 2)
score_text = font.render("score:" + str(score), True, green, darkred)
score_rect = score_text.get_rect()
score_rect.topleft = (5, 10)
game_over = font.render("game-over", True, red)
game_rect = game_over.get_rect()
game_rect.center = (width // 2, height // 2)
continue_text = font.render("Rrest", True, green)
continue_rect = continue_text.get_rect()
continue_rect.center = (width // 2, height // 2 + 64)
# 背景音乐
pick_up_sound = pygame.mixer.Sound("music/Letting Go - 蔡健雅.mp3")
# 图片大小
apple_coord = (500, 500, snake_size, snake_size)
apple_rect = pygame.draw.rect(display, red, apple_coord)
head_coord = (head_x, head_y, snake_size, snake_size)
head_rect = pygame.draw.rect(display, green, head_coord)
body_coords = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1 * snake_size
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = snake_size
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1 * snake_size
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = snake_size
    # 身体给索引
    body_coords.insert(0, head_coord)
    body_coords.pop()

    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, snake_size, snake_size)
    # 结束游戏
    if head_rect.left < 0 or head_rect.right > width or head_rect.top < 0 or head_rect.bottom > height:
        display.blit(game_over, game_rect)
        display.blit(continue_text, continue_rect)
        pygame.display.update()
        is_push = True
        while is_push:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    head_x = width // 2
                    head_y = height // 2 + 10
                    head_coord = (head_x, head_y, snake_size, snake_size)
                    body_coords = []
                    snake_dy = 0
                    snake_dx = 0
                    is_push = False
                if event.type == pygame.QUIT:
                    is_push = False
                    running = False

    # 碰撞
    if head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()
        apple_x = random.randint(0, width - snake_size)
        apple_y = random.randint(0, height - snake_size)
        apple_coord = (apple_x, apple_y, snake_size, snake_size)
        body_coords.append(apple_coord)
    # 分数
    score_text = font.render("score:" + str(score), True, green, darkred)
    display.fill(white)
    display.blit(score_text, score_rect)
    display.blit(tile_text, tile_rect)
    for body in body_coords:
        pygame.draw.rect(display, green, body)
    head_rect = pygame.draw.rect(display, green, head_coord)
    apple_rect = pygame.draw.rect(display, red, apple_coord)
    pygame.display.update()
    clock.tick(10)
pygame.quit()
