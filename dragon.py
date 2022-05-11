import pygame, random
pygame.init()
width = 1000
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("game")
# 帧率
clock = pygame.time.Clock()
# 移动距离
play_start_lives = 5
play_velocity = 10
coin_start_velocity = 10
coin_acc = .5
buff = 100
score = 0
play_lives = play_start_lives
coin_velocity = coin_start_velocity
# 颜色
green = (0, 255, 0)
darkgreen = (10, 50, 0)
white = (255, 255, 255)
black = (0, 0, 0)
# 字体样式
font = pygame.font.SysFont("arial", 30)
# 文本内容
score_text = font.render("Score" + str(score), True, green, darkgreen)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)
title_text = font.render("feed the dragon", True, green, white)
title_rect = title_text.get_rect()
title_rect.centerx = width // 2
lives_text = font.render("lives" + str(play_lives), True, green, darkgreen)
lives_rect = lives_text.get_rect()
lives_rect.topright = (width - 40, 10)
title_rect.y = 10
game_over = font.render("gameover", True, green, darkgreen)
game_over_rect = game_over.get_rect()
game_over_rect.center = (width // 2, height // 2)
continue_text = font.render("press any key to play again", True, green, darkgreen)
continue_rect = continue_text.get_rect()
continue_rect.center = (width // 2, height // 2 + 32)
# 背景音乐
coin_sound = pygame.mixer.Sound("孤勇者 - 陈奕迅.mp3")
miss_sound = pygame.mixer.Sound("Letting Go - 蔡健雅.mp3")
miss_sound.set_volume(.1)
pygame.mixer.music.load("钢琴 BGM 黑人抬棺 全网最火黑人抬棺,专业团队。初听不识曲中意,再听已是棺中人 - 泡泡钢琴APP.mp3")
# 图片
image = pygame.image.load("imge/lt.jpg")
rect = image.get_rect()
rect.left = 32
rect.centery = width // 2
image_2 = pygame.image.load("imge/jb.jpeg")
rect_2 = image_2.get_rect()
rect_2.x = width + buff
rect_2.y = random.randint(50, height - 25)
# 游戏主循环
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 键盘龙头操作
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and rect.top > 50:
        rect.y -= play_velocity
    if keys[pygame.K_DOWN] and rect.bottom < height:
        rect.y += play_velocity
    # 移动金币
    if rect_2.x < 0:
        play_lives -= 1
        miss_sound.play(1)
        rect_2.x = width + buff
        rect_2.y = random.randint(50, height - 25)
    else:
        rect_2.x -= coin_velocity
    # 碰撞
    if rect.colliderect(rect_2):
        score += 1
        coin_sound.play()
        coin_velocity += coin_acc
        rect_2.x = width + buff
        rect_2.y = random.randint(50, height - 25)
    # 动态更新
    score_text = font.render("score:" + str(score), True, green, darkgreen)
    lives_text = font.render("render:" + str(play_lives), True, green, darkgreen)
    # 结束游戏
    if play_lives == 0:
        display.blit(game_over, game_over_rect)
        display.blit(continue_text, continue_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    play_lives = play_start_lives
                    rect.y = height // 2
                    coin_velocity = coin_start_velocity
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
    # 样式
    display.fill(black)
    # 顶部
    display.blit(score_text, score_rect)
    display.blit(title_text, title_rect)
    display.blit(lives_text, lives_rect)
    pygame.draw.line(display, white, (0, 50), (width, 50), 2)
    # 图片
    display.blit(image, rect)
    display.blit(image_2, rect_2)
    # 刷新
    pygame.display.update()
    clock.tick(90)
pygame.quit()
