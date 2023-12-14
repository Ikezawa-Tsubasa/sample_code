import pygame as pg
from random import randint
from time import time

#演習問題１

WIDTH = 800
HEIGHT = 600
"""
class Object(pg.sprite.Sprite):
    def __init__(self, vx=0, vy=0):
        super().__init__()
        self.vx = vx
        self.vy = vy

    def load_image(self, image_path):
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect()

    def update(self, screen:pg.Surface):
        self.rect.move_ip(self.vx, self.vy)
        screen.blit(self.image, self.rect)

"""
"""
def main():
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg = Object()
    bg.load_image("bg.png")
    bg.image = pg.transform.rotozoom(bg.image, 0, 2.5)
    player = Player()
    esa = Esa()
    while True:
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
        if pg.sprite.collide_rect(player, esa):
            esa = Esa()
        
        bg.update(screen)
        esa.update(screen)
        player.update(screen, keys)

        pg.display.update()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
"""

#演習問題2

class Object(pg.sprite.Sprite):
    def __init__(self, vx=0, vy=0):
        super().__init__()
        self.vx = vx
        self.vy = vy

    def load_image(self, image_path):
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect()

    def update(self, screen:pg.Surface):
        if sum(check_frameout(self, self.vx, self.vy)) == 0:
            self.rect.move_ip(self.vx, self.vy)
        
        screen.blit(self.image, self.rect)
class Player(Object):

    def __init__(self):
        super().__init__()
        self.image = pg.Surface((30, 30))
        self.rect = pg.draw.rect(self.image, (0, 0, 0), (0, 0, 30, 30))
    
    
    def update(self, screen, key_lst):
        sum_mv = check_key(key_lst)
        self.vx, self.vy= sum_mv[0]*5, sum_mv[1]*5
        super().update(screen)

class Esa(Object):
    def __init__(self):
        super().__init__()
        rad = randint(5, 15)
        self.image = pg.Surface((rad*2, rad*2))
        self.rect = pg.draw.circle(self.image, (randint(0, 255), randint(0, 255), randint(0, 255)), (rad, rad), rad)
        self.image.set_colorkey(0)
        self.rect.center = randint(0, WIDTH), randint(0, HEIGHT)

def check_key(key_list:dict):
    sum_mv=[0, 0]
    if True in key_list:
        if key_list[pg.K_UP]:
            sum_mv[1] -= 1
        if key_list[pg.K_DOWN]:
            sum_mv[1] += 1
        if key_list[pg.K_LEFT]:
            sum_mv[0] -= 1
        if key_list[pg.K_RIGHT]:
            sum_mv[0] += 1
    return sum_mv

class Score(Object):
    def __init__(self):
        super().__init__()
        self.font = pg.font.Font(None, 50)
        self.color = (0, 0, 255)
        self.score = 0
        self.image = self.font.render(f"Score: {self.score}", color=self.color)
        self.rect = self.image.get_rect()
        self.rect.center = 100, HEIGHT-50
        
    def score_up(self, add):
        self.score += add

    def update(self, screen):
        self.image = self.font.render(f"Score: {self.score}", 0, self.color)
        super().update(screen)

class Elapsed_time(Object):
    def __init__(self):
        super().__init__()
        self.font = pg.font.Font(None, 25)
        self.color = 0
        self.start_time = time()
        self.image = self.font.render(f"Time: {self.start_time}", 0, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = 150, 50
    
    def update(self, screen):
        self.image = self.font.render(f"Time: {int(time() - self.start_time)}", 0, self.color)
        super().update(screen)
        

class Bullet(Object):
    def __init__(self,pl, vx=0, vy=0, rad=5):
        super().__init__(vx, vy)
        self.image = pg.Surface((rad*2, rad*2))
        self.rect = pg.draw.rect(self.image, 255, (0, 0, rad*2, rad*2))
        pg.draw.circle(self.image, (255, 0, 0), (rad, rad), int(rad))
        pg.draw.circle(self.image, 0, (rad, rad), int(rad*(3/5)))
        pg.draw.circle(self.image, (255, 0, 0), (rad, rad), int(rad/5))
        self.image.set_colorkey(255)
        self.rect.center = pl.rect.center
    
    
        
        
        
class Item(Object):
    def __init__(self):
        super().__init__()
        rad = randint(5, 15)
        self.image = pg.Surface((rad*2, rad*2))
        self.rect = pg.draw.rect(self.image, (randint(0, 255), randint(0, 255), randint(0, 255)), (0, 0, rad*2, rad*2))
        #self.image.set_colorkey(0)
        self.rect.center = randint(0, WIDTH), randint(0, HEIGHT)




def check_frameout(obj:Object, vx=0, vy=0):
    ret = [0, 0] #x軸, y軸のフレームアウト判定
    if obj.rect.left+vx<0:
        ret[0] = -1
    elif WIDTH<obj.rect.right+vx:
        ret[0] = +1
    if obj.rect.top+vy<0:
        ret[1] = -1
    elif HEIGHT<obj.rect.bottom+vy:
        ret[1] = +1
    return ret



def main():
    #pg.display.set_caption("test")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    bg = Object()
    bg.load_image("bg.png")
    bg.image = pg.transform.rotozoom(bg.image, 0, 2.5)
    me = Player()
    esa = Esa()
    score = Score()
    item = Item()
    bul = pg.sprite.Group()
    time=Elapsed_time()
    bul_flag = False
    bul_size = 5
    while True:
        key_lst = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
            
        if pg.sprite.collide_rect(me, esa):
            esa = Esa()
            score.score_up(10)
        
        if pg.sprite.collide_rect(me, item):
            item = Item()
            bul_size += 1
        
        if len(bul) != 0:
            for b in pg.sprite.spritecollide(esa, bul, True):
                esa = Esa()
                score.score_up(10)

        if key_lst[pg.K_a]:
            if not bul_flag:
                bul_flag = True
                bul.add(Bullet(me,2, rad=bul_size))
        else:
            bul_flag = False

        bg.update(screen)
        if len(bul) != 0:
            bul.update(screen)
            for b in bul:
                if check_frameout(b, b.vx, b.vy) != [0, 0]:
                    bul.remove(b)
        score.update(screen)
        time.update(screen)
        esa.update(screen)
        item.update(screen)
        me.update(screen, key_lst)

        #print(len(bul))
        pg.display.update()
        clock.tick(100)
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
