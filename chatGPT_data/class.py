import pygame
from pygame.locals import *
class Player:
    def __init__(self, x, y, width, height, color, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def update(self, direction):
        self.rect.x += self.speed * direction
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
class Bullet:
    def __init__(self, x, y, width, height, color, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed
        self.is_active = False
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def update(self):
        self.rect.y -= self.speed
    
    def fire(self, x, y):
        self.rect.center = (x, y)
        self.is_active = True
class Enemy:
    def __init__(self, x, y, width, height, color, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed *= -1
            self.rect.y += 20
# ゲームの初期化
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
# ゲームオブジェクトの作成
player = Player(screen_width // 2 - 25, screen_height - 50, 50, 30, (0, 255, 0), 5)
bullet = Bullet(0, 0, 10, 20, (255, 0, 0), 10)
enemies = []
for row in range(5):
    for col in range(10):
        x = col * 70 + 50
        y = row * 50 + 50
        enemy = Enemy(x, y, 40, 30, (0, 0, 255), 2)
        enemies.append(enemy)
# ゲームループ
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE and not bullet.is_active:
                bullet.fire(player.rect.centerx, player.rect.top)
    
    keys = pygame.key.get_pressed()
    direction = keys[K_RIGHT] - keys[K_LEFT]
    player.update(direction)
    
    if bullet.is_active:
        bullet.update()
        if bullet.rect.bottom < 0:
            bullet.is_active = False
    
    for enemy in enemies:
        enemy.update()
        if enemy.rect.colliderect(player.rect):
            running = False
        if bullet.is_active and enemy.rect.colliderect(bullet.rect):
            bullet.is_active = False
            enemies.remove(enemy)
    
    screen.fill((0, 0, 0))
    
    player.draw(screen)
    if bullet.is_active:
        bullet.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    
    pygame.display.flip()
pygame.quit()
