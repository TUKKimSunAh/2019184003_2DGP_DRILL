from pico2d import *
import Game_Framework
import Logo_State


class Mario:
    global Check_Dir, Check_Move, bJump, Check_Jump

    def __init__(self):
        self.x, self.y = 20, 800
        self.Speed = 0.5
        self.frame = 0
        self.Force = 1

        self.Idle_R = load_image('Mario_R.png')
        self.Idle_L = load_image('Mario_L.png')
        self.Walk_R = load_image('Mario_WalkR.png')
        self.Walk_L = load_image('Mario_WalkL.png')
        self.Jump_R = load_image('Mario_JumpR.png')
        self.Jump_L = load_image('Mario_JumpL.png')

    def update(self):

        self.y -= self.Force

        if Check_Move == 1:
            self.frame = (self.frame + 1) % 3
            self.x = self.x + self.Speed

        elif Check_Move == -1:
            self.frame = (self.frame + 1) % 3
            self.x = self.x - self.Speed

        elif bJump:
            self.y = self.y + self.Force * 2

    def draw(self):
        if Check_Dir == 1:
            if Check_Move == 0:
                self.Idle_R.draw(self.x, self.y)
            elif Check_Move == 1:
                self.Walk_R.clip_draw(self.frame * 32, 0, 32, 32, self.x, self.y)

        elif Check_Dir == -1:
            if Check_Move == 0:
                self.Idle_L.draw(self.x, self.y)
            elif Check_Move == -1:
                self.Walk_L.clip_draw(self.frame * 32, 0, 32, 32, self.x, self.y)

        if bJump:
            if Check_Jump == 1:
                self.Jump_R.draw(self.x, self.y)
            elif Check_Jump == -1:
                self.Jump_L.draw(self.x, self.y)

        # elif bJump:
        #     if Check_Dir == -1:
        #         self.Jump_L.draw(self.x, self.y)
        #     elif Check_Dir == 1:
        #         self.Jump_R.draw(self.x, self.y)


class Stage1:
    def __init__(self):
        self.x, self.y = 4000, 600
        self.Stage_1 = load_image('Map_Stage1.png')

    def update(self):
        pass

    def draw(self):
        self.Stage_1.draw(self.x // 2, self.y // 2)


class Long_Block:
    def __init__(self):
        self.x, self.y = 722, 85
        self.Long_Block = load_image('Long_Block.png')

    def update(self):
        pass

    def draw(self):
        self.Long_Block.draw(self.x / 2, self.y / 2)


class Bricks:
    def __init__(self):
        self.x, self.y = 34, 34
        self.Bricks = load_image('Bricks.png')

    def update(self):
        pass

    def draw(self):
        self.Bricks.draw(self.x / 2, self.y / 2)


class Iron:
    def __init__(self):
        self.x, self.y = 34, 34
        self.Iron = load_image('Iron.png')

    def update(self):
        pass

    def draw(self):
        self.Iron.draw(self.x / 2, self.y / 2)


class QBox1:
    def __init__(self):
        self.x, self.y = 34, 34
        self.QBox1 = load_image('QBox1.png')

    def update(self):
        pass

    def draw(self):
        self.QBox1.draw(self.x / 2, self.y / 2)


class QBox2:
    def __init__(self):
        self.x, self.y = 34, 34
        self.QBox2 = load_image('QBox2.png')

    def update(self):
        pass

    def draw(self):
        self.QBox2.draw(self.x / 2, self.y / 2)


class QBox3:
    def __init__(self):
        self.x, self.y = 34, 34
        self.QBox3 = load_image('QBox3.png')

    def update(self):
        pass

    def draw(self):
        self.QBox3.draw(self.x / 2, self.y / 2)


class QBox_Die:
    def __init__(self):
        self.x, self.y = 34, 34
        self.QBox_Die = load_image('QBox_Die.png')

    def update(self):
        pass

    def draw(self):
        self.QBox_Die.draw(self.x / 2, self.y / 2)


def handle_events():
    global Check_Dir, Check_Move, bJump, Check_Jump
    global mario

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Game_Framework.change_state(Logo_State)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            Check_Dir = 1
            Check_Move = 1

        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            Check_Move = 0

        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            Check_Dir = -1
            Check_Move = -1

        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            Check_Move = 0

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if Check_Dir == 1:
                Check_Jump = 1
            elif Check_Dir == -1:
                Check_Jump = -1

            bJump = True

        elif event.type == SDL_KEYUP and event.key == SDLK_UP:
            bJump = False
            Check_Jump =0



mario = None
stage1 = None
running = None

# 마리오의 방향을 확인하기 위한 변수 | 오른쪽일 경우 1, 왼쪽일 경우 -1
Check_Dir = 1
# 마리오의 행동을 확인하기 위한 변수 | 아이들일 경우 0, 오른쪽일 경우 1, 왼쪽일 경우 -1
Check_Move = 0
# 마리오의 점푸를 확인하기 위한 변수 | 아이들일 경우 0, 오른쪽 점프할 경우 1, 왼쪽 점프할 경우 -1
Check_Jump = 1

# 마리오 점프 여부 | True, False로 판단
bJump = False

open_canvas()


def enter():
    global mario, running, stage1, long_block

    mario = Mario()
    stage1 = Stage1()
    long_block = Long_Block()
    # grass = Grass()
    running = True


def exit():
    global mario, stage1

    del mario
    del stage1


def update():
    mario.update()
    stage1.update()
    long_block.update()


def draw():
    clear_canvas()
    stage1.draw()
    mario.draw()
    long_block.draw()
    update_canvas()


open_canvas()

while running:
    handle_events()
    update()
    draw()
exit()

# finalization code
close_canvas()
