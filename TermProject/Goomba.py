from pico2d import *
import Game_World


class Goomba:
    image = None

    def __init__(self, x, y):
        if Goomba.image == None:
            Goomba.image = load_image('Goomba.png')

        self.frame = 0
        # 시작은 왼쪽으로 충돌시 오른 쪽 (-1)로 변경
        self.DirCheck = 1
        self.Velocity = 0.1
        self.width, self.height = 26, 26
        self.x, self.y = x, y

        self.Force = 0
        self.Gravity = 0.09

    def Set_Gravity(self):
        self.y += self.Force
        self.Force -= self.Gravity
        pass

    def Change_Dir(self, CheckDir):
        self.DirCheck = CheckDir

    def get_bb(self):
        return self.x - 13, self.y - 13, self.x + 13, self.y + 13

    def update(self):
        self.frame = (self.frame + 1) % 2

        self.Force += 0.01
        self.Set_Gravity()

        if self.DirCheck == 1:
            self.x += self.Velocity
        if self.DirCheck == -1:
            self.x -= self.Velocity

        if self.x < 0 or self.x > 800:
            Game_World.Remove_Object(self)
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 30, self.x, self.y)
