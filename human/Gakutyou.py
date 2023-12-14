import pygame as pg
import sys
import random
import time
import math

class Gakutyou(pg.sprite.Sprite):
    """
    学長のクラス（スプライト継承済み）
    コンストラクタでは位置と大きさ（倍率）を指定して作成
    """

    BACK_COLOR = (120, 250, 120)
    COOL_TIME_BASE = 360

    def __init__(self, position: tuple[int, int], size: float, hardMode) -> None:
        super().__init__()
        gImg = pg.image.load("images/gakutyou.png") # 学長画像
        cImg = pg.image.load("images/g_cloud.png") # 学長が乗る雲画像
        self.image = pg.Surface((300, 340)) # 学長の画像を張り付ける用のSurface
        self.image.fill(Gakutyou.BACK_COLOR)
        self.image.blit(pg.transform.rotozoom(gImg, 0, 300 / gImg.get_width() * 1.9), (-210,-70))
        self.image.blit(pg.transform.rotozoom(cImg, 0, 340 / cImg.get_width() * 1.05), (-25,65))
        self.rect = self.image.get_rect()
        self.rect.center = position

        eyeLight = pg.image.load("images/eye_light.png") # 目の光をロード
        eyeLight = pg.transform.rotozoom(eyeLight, 0, 0.035) # サイズ調整
        self.images: list[pg.surface.Surface] = []
        # ここからフレームごとに切り替える学長画像のリストを作成
        for i in range(50): # 光の画像の立ち上がり
            currentImg = self.image.copy()
            currentSurf = pg.Surface((300, 100))
            currentSurf.blit(eyeLight, (117, 40))
            currentSurf.blit(eyeLight, (150, 40))
            currentSurf.set_colorkey((0, 0, 0))
            currentSurf.set_alpha(i * 5)
            currentImg.blit(currentSurf, (0, 0))
            self.images.append(currentImg)
        for i in range(20): # 点灯状態を20フレーム
            self.images.append(self.images[49].copy())
        for i in range(50)[::-1]: # 立ち下がり部分
            self.images.append(self.images[i].copy())
        self.images = [pg.transform.rotozoom(x, 0, size) for x in self.images]
        for i in self.images: # 一気に背景透過
            i.set_colorkey(Gakutyou.BACK_COLOR)
        self.image = self.images[0] # 最初の画像は0番目で固定
        self.timer = 0 # Updateごとに1増やすタイマーを設定
        self.attackTimer = -1 # 攻撃時間を設定（攻撃時以外は-1）
        self.isReady = False # 攻撃中かどうか
        self.coolTime = Gakutyou.COOL_TIME_BASE + hardMode * -120
        self.channel = pg.mixer.Channel(1)

    def update(self):
        """
        update関数のオーバーライド\n
        毎フレーム呼び出してください
        """
        if self.timer >= self.coolTime or self.isReady:
            # 学長の攻撃が始まる時間になったらタイマーをリセット
            self.timer = 0 
            self.isReady = True
            self.image = self.images[50]
        else:
            self.timer += 1
            self.image = self.images[int(self.timer * ((self.timer // 120 + 1) ** 2)) % 120] # タイマーに応じて画像を変更
            if int(self.timer * ((self.timer // 120 + 1) ** 2)) % 120 <= 10:
                self.channel.play(pg.mixer.Sound("sounds/pika.mp3"))
        
    def get_isReady(self):
        """
        クールタイムが終わったかをBool型で返す関数、Trueの時呼び出されると一定時間Trueを返し続ける\n
        引数：無し\n
        戻り値：True(攻撃できるとき) or False(攻撃できないとき)
        """
        if self.attackTimer < 0 and not self.isReady:
            return False
        if self.attackTimer >= 0:
            self.attackTimer -= 1 # attackTimerが設定されている間は1ずつ減算
            if self.attackTimer < 0:
                self.isReady = False # タイマーが0未満になったら攻撃を終了
            return True
        elif self.isReady:
            self.attackTimer = 100 # 攻撃の時間を100に設定
            return True




class background(pg.sprite.Sprite):
    def __init__(self):
        self.image= pg.image.load("images/sky_img.png")#背景画像を受け取る
        self.image = pg.transform.rotozoom(self.image, 0, 1.0)#背景画像の大きさ修正
        self.rect = self.image.get_rect()

    def update(self, movevalue:float):
        self.rect.move_ip(-movevalue, 0)#横方向に画像をキャラに合わせて動かす

class Character(pg.sprite.Sprite):
    """
    操作キャラクターに関するクラス
    """
    def __init__(self, xy: tuple[int, int]):
        """
        操作キャラクターSurfaceを描画する
        引数 xy：キャラクターの初期位置
        """
        super().__init__()
        self.image = pg.transform.flip(pg.transform.rotozoom(pg.image.load("images/character1.png"), 0, 0.5), True, False)
        self.rect = self.image.get_rect()
        self.rect.center = xy
        self.dx = 10
        self.images: list[pg.Surface] = []
        for i in range(1, 4):
            self.images.append(pg.transform.flip(pg.transform.rotozoom(pg.image.load(f"images/character{i}.png"), 0, 0.5), True, False))
        self.channel = pg.mixer.Channel(3)

    def calc_mv(self, key_lst: list[bool], bg: pg.sprite.Sprite, hardMode):
        """
        押下キーに応じてキャラクターの移動量を返す関数
        引数１ key_lst：押下キーの真理値リスト
        """
        mv = 0
        # 左シフトを押すと加速
        if key_lst[pg.K_LSHIFT] and not hardMode:
            self.dx = 30
        else:
            self.dx = 15
        if key_lst[pg.K_LEFT]:
            mv = self.dx
        elif key_lst[pg.K_RIGHT]:
            mv = -self.dx
        if bg.rect.x >= 0 and mv > 0:
            mv = 0
        return mv

    def update(self, num: int, screen: pg.Surface, isHardmode: bool):
        """
        障害物に当たった時に画像を切り替える
        引数１ num：画像の番号
        引数２ screen：画面Surface
        """
        self.image = self.images[num-1]
        if num in (2, 3):
            # キャラクターの状態が2か3なら効果音を再生
            pg.mixer.Channel(2).stop()
            seName = "sounds/"
            if num == 2:
                seName += "damage.mp3"
                self.rect.move_ip((self.images[0].get_width() - self.images[1].get_width()), 0)
                self.channel.play(pg.mixer.Sound(seName), maxtime=1000)
                return
            elif num == 3 and not isHardmode:
                seName += "normalClear.mp3"
            elif num == 3 and isHardmode:
                seName += "hardClear.mp3"
            self.channel.play(pg.mixer.Sound(seName))



WITDH = 1600
HEIGHT = 900
STAGE_WIDTH = 7000  # ステージの横幅
TREE_BOTTOM = 47
WALL_NUM = 10  # 木の数
screen: pg.Surface = None

class Wall(pg.sprite.Sprite):
    """
    遮蔽物(以下、木)の描画、判定処理
    """
    def __init__(self, screen: pg.Surface, number):
        """
        遮蔽物(木)を描画
        引数: screen: 画面Surface
        """
        super().__init__()
        self.image = pg.transform.rotozoom(pg.image.load("images/tree.png"), 0, 0.5)  # 木の画像を読み込む
        self.rect = self.image.get_rect()  # 木のrectを作成
        self.rect.bottom = HEIGHT - TREE_BOTTOM  # 木のY座標を固定
        treeExistWidth = STAGE_WIDTH // WALL_NUM
        self.rect.centerx = random.randint(treeExistWidth * number, treeExistWidth * (number + 2)) # 木のX座標を決定。一定間隔の間にランダムで生成
    
    def update(self, screen: pg.Surface, mv):
        """
        ユーザの操作に応じで木の描画位置を変更
        引数1 key_lst: 押下キーの真理値リスト
        引数2 screen: 画面Surface
        """
        # 旧版
        # self.speedx = 0  # もし、キーボードを押していなければ移動しない
        # if key_lst[pg.K_LEFT]:  # もし、左矢印を押していたら...
        #     self.speedx = 10  # 右に20動く
        # if key_lst[pg.K_RIGHT]:  # もし、右矢印を押していたら...
        #     self.speedx = 10 * (-1)  # 左に20動く

        self.rect.centerx += mv  # 木の位置を更新




class Start_menu:
    """
    スタート画面を表示させるクラス
    """
    def __init__(self):
        """
        フォント、メニュータイトルの表示
        """
        self.font = pg.font.Font("fonts/onryou.TTF", 100)
        self.menu_title = self.font.render("学長が転んだ", True, (255, 255, 255))
        creditsFont = pg.font.Font("fonts/POP.ttf", 20)
        self.menu_credit = creditsFont.render("効果音：OtoLogic - https://otologic.jp/", False, (255, 255, 255))
        
    def button(self, screen: pg.Surface, num:int):
        """
        どのボタンを選択しようとしているのかを表示する
        引数1 screen 画面の表示
        引数2 num どのボタンが選択中か
        """
        if num == 0:
            self.left_button = self.font.render("スタート", True, (255, 0, 0))
            self.right_button = self.font.render("ヤメル",True, (255, 255, 255))
        elif num == 1:
            self.left_button = self.font.render("スタート", True, (255, 255, 255))
            self.right_button = self.font.render("ヤメル",True, (255, 0, 0))
        elif num == 2:
            self.left_button = self.font.render("ふつう", True, (255, 0, 0))
            self.right_button = self.font.render("むずかしい",True, (255, 255, 255))
        elif num == 3:
            self.left_button = self.font.render("ふつう", True, (255, 255, 255))
            self.right_button = self.font.render("むずかしい",True, (255, 0, 0))
        
        screen.fill((0, 0, 0))
        screen.blit(self.menu_title, (WITDH/2 - self.menu_title.get_width()/2, HEIGHT/2 - self.menu_title.get_height()))
        screen.blit(self.menu_credit, (WITDH - self.menu_credit.get_width() - 30, HEIGHT - self.menu_credit.get_height()))
        screen.blit(self.left_button, (WITDH/3 - self.left_button.get_width()/2, HEIGHT/2 + self.left_button.get_height()))
        screen.blit(self.right_button, (WITDH/3 * 2 - self.right_button.get_width()/2, HEIGHT/2 + self.right_button.get_height()))


class Enemy(pg.sprite.Sprite):
    """
    道中の障害物(おさかなさん等)に関するクラス
    """

    def __init__(self, hardMode: bool, bg: pg.sprite.Sprite):
        super().__init__()
        pict= pg.image.load(random.choice(("images/ojama.png",) + ("images/frogFSM.png",) * (hardMode * (bg.rect.left < -3000)))) # 敵キャラの抽選
        self.image = pg.transform.rotozoom(pict, 0, 80000 / (pict.get_width() * pict.get_height()))   # 障害物の画像読み込み
        self.rect = self.image.get_rect()
        self.rect.center = WITDH + 100, HEIGHT / 4
        self.vy = +40
        self.ay = +1.0
        self.vx = -4 + hardMode * -8
        self.radian = 0
        self.randomJump = random.randint(100, 200)

    def update(self, mv_value):
        """
        お魚が地面ではねるところ
        引数screen：画面Surface
        """
        self.radian += self.vx * self.randomJump / 100
        self.rect.centerx += self.vx + mv_value
        self.rect.bottom = -abs(math.sin(self.radian / self.randomJump)) * (870 - self.image.get_height()) + 870
        
        
def displayInit():
    global screen
    pg.display.set_caption("学長が転んだ")
    screen = pg.display.set_mode((WITDH, HEIGHT))

def main():
    global screen
    # ここからメニュー画面
    pg.mixer.init(channels=10)
    pg.mixer.music.load("sounds/menuBGM.wav")
    pg.mixer.music.play(-1)
    start_menu = Start_menu()
    game_state = "menu_start"
    start_menu.button(screen, 0)
    while game_state != "choiceDifficulty":
        pg.display.update()
        key_lst = pg.key.get_pressed()
        for event in pg.event.get():
            if (event.type == pg.KEYDOWN and event.key == pg.K_RIGHT):#右キーを押下で設定画面に移れる状態にする
                start_menu.button(screen, 1)
                game_state = "menu_end"
            if(event.type == pg.KEYDOWN and event.key == pg.K_LEFT):#左キーを押下でゲーム画面に移れる状態にする
                start_menu.button(screen, 0)
                game_state = "menu_start"
            if event.type == pg.KEYDOWN and event.key in (pg.K_SPACE, pg.K_ESCAPE, pg.K_DOWN) and game_state == "menu_start":
                game_state = "choiceDifficulty"
            if event.type == pg.KEYDOWN and event.key in (pg.K_SPACE, pg.K_ESCAPE, pg.K_DOWN) and game_state == "menu_end":    
                return "end"
    # 難易度選択
    isHardmode = False
    game_state = "menu_normal"
    start_menu.button(screen, 2)
    while game_state != "running":
        pg.display.update()
        key_lst = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:#右キーを押下でふつう画面に移れる状態にする
                start_menu.button(screen, 3)
                game_state = "menu_hard"
            if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:#左キーを押下でむずかしい画面に移れる状態にする
                start_menu.button(screen, 2)
                game_state = "menu_normal"
            if event.type == pg.KEYDOWN and event.key in (pg.K_SPACE, pg.K_ESCAPE, pg.K_DOWN) and game_state == "menu_normal":
                game_state = "running"
                isHardmode = False
            if event.type == pg.KEYDOWN and event.key in (pg.K_SPACE, pg.K_ESCAPE, pg.K_DOWN) and game_state == "menu_hard":    
                game_state = "running"
                isHardmode = True
    pg.mixer.music.stop()
    # ここからゲームスタート
    gakutyou = Gakutyou((1000, 200), 1, isHardmode) # 学長インスタンスを作成
    character = ch.Character([200, 704])
    bg = background()
    emy: Enemy = None
    trees = pg.sprite.Group() # 木のグループ

    tmr = 0
    clock = pg.time.Clock()
    clock.get_time()
    for i in range(WALL_NUM):  # WALL_NUMの分だけ繰り返す
        trees.add(Wall(screen, i))  # 木の情報を追加

    mixer1 = pg.mixer.Channel(2)
    mixer1.play(pg.mixer.Sound(f"sounds/ingameBGM{'fast' * isHardmode}.wav"), -1)
    while True:
        if emy is None:
            emy = Enemy(isHardmode, bg)
        key_lst = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return "end"
        mv = character.calc_mv(key_lst, bg, isHardmode)
        bg.update(-mv)
        screen.blit(bg.image,bg.rect)
        gakutyou.update() # 学長インスタンスの更新
        if gakutyou.get_isReady(): # 学長の攻撃中
            mixer1.pause()
            shadeSurface = pg.Surface((WITDH, HEIGHT))
            shadeSurface.fill((0, 0, 0))
            shadeSurface.set_alpha(100)
            screen.blit(shadeSurface, (0, 0))
            # 隠れられているか判定
            if len(pg.sprite.spritecollide(character, trees, False)) == 0:
                game_state = "game_over"
        else:
            mixer1.unpause()
        screen.blit(gakutyou.image, gakutyou.rect) # 学長インスタンスを描画
        trees.update(screen, mv)  # 木の位置を更新する
        trees.draw(screen)

        # クリア
        if bg.rect.x <= -6800:
            character.update(3, screen, isHardmode)   
            screen.blit(character.image, character.rect) # キャラクター描画        
            pg.display.update()
            time.sleep(2)
            return "clear"

        
        # キャラクターと障害物の衝突判定
        if math.sqrt((character.rect.centerx - emy.rect.centerx)**2
                     + (character.rect.centery - emy.rect.bottom)**2) <= 170 \
                     and (character.rect.centerx - emy.rect.centerx) < 100: # 当たり判定の調節
            game_state = "game_over"
        
        if emy is not None:
            emy.update(mv)
            screen.blit(emy.image, emy.rect)
            if emy.rect.right <= 0:
                emy = None #画面外に出たら自身をkill

        # ゲームオーバー判定
        if game_state == "game_over":
            fonto = pg.font.Font("fonts/onryou.TTF", 200)
            txt = fonto.render("退学", True, (255, 0, 0))
            txt_rect = txt.get_rect()
            txt_rect.center = (WITDH / 2, HEIGHT / 2)
            screen.blit(txt, txt_rect)
            character.update(2, screen, isHardmode)
            screen.blit(character.image, character.rect)
            pg.display.update()
            time.sleep(2)
            return "damage"
        screen.blit(character.image, character.rect) # キャラクター描画
        clock.tick(50)
        pg.display.update()
        tmr += 1
        

if __name__ == "__main__":
    pg.init()
    displayInit()
    status = "first"
    while status != "end":
        status = main()
        pg.mixer.stop()
    pg.quit()
    sys.exit()