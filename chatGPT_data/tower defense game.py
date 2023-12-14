import pygame
import random
# ゲーム画面のサイズ
width = 800
height = 600
# 色の定義
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
# ゲーム画面の設定
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tower Defense Game")
clock = pygame.time.Clock()
class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - 20)
        self.rect.y = 0
        self.speed = random.randint(1, 3)
    def update(self):
        self.rect.y += self.speed
def game_loop():
    game_over = False
    tower = Tower(width // 2, height - 50)
    tower_group = pygame.sprite.Group()
    tower_group.add(tower)
    enemy_group = pygame.sprite.Group()
    score = 0
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            tower.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            tower.rect.x += 5
        if random.randint(0, 100) < 5:
            enemy = Enemy()
            enemy_group.add(enemy)
        enemy_group.update()
        for enemy in enemy_group:
            if pygame.sprite.collide_rect(enemy, tower):
                enemy_group.remove(enemy)
                score += 1
        screen.fill(black)
        tower_group.draw(screen)
        enemy_group.draw(screen)
        font = pygame.font.Font(None, 24)
        text = font.render("Score: " + str(score), True, white)
        screen.blit(text, (10, 10))
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
game_loop()
