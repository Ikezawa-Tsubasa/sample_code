import pygame
import random
import time
pygame.init()
# ゲーム画面のサイズ
width = 800
height = 600
# 色の定義
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
# ゲーム画面の設定
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Typing Game")
clock = pygame.time.Clock()
def generate_word():
    words = ["apple", "banana", "cherry", "grape", "orange", "melon", "kiwi", "pineapple", "strawberry", "watermelon"]
    return random.choice(words)
def draw_word(word, word_x, word_y):
    font = pygame.font.Font(None, 36)
    text = font.render(word, True, white)
    screen.blit(text, (word_x, word_y))
def game_loop():
    game_over = False
    word = generate_word()
    word_x = (width - len(word) * 20) // 2
    word_y = height // 2
    score = 0
    start_time = time.time()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                elif event.key == pygame.K_RETURN:
                    word = generate_word()
                    word_x = (width - len(word) * 20) // 2
                    word_y = height // 2
                else:
                    if event.unicode == word[0]:
                        word = word[1:]
                        score += 1
                        if len(word) == 0:
                            word = generate_word()
                            word_x = (width - len(word) * 20) // 2
                            word_y = height // 2
        screen.fill(black)
        draw_word(word, word_x, word_y)
        elapsed_time = time.time() - start_time
        font = pygame.font.Font(None, 24)
        text = font.render("Score: " + str(score), True, white)
        screen.blit(text, (10, 10))
        text = font.render("Time: " + str(int(elapsed_time)) + "s", True, white)
        screen.blit(text, (10, 40))
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
game_loop()
