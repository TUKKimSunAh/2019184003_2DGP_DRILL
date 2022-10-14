from pico2d import *
import Game_Framework
import Logo_State


# class Grass:
#     def __init__(self):
#         self.image = load_image('grass.png')
#
#     def draw(self):
#         self.image.draw(400, 30)

class Mario:
    global Check_Dir, Check_Move

    def __init__(self):
        self.x, self.y = 0, 90
        self.Speed = 10
        self.frame = 0

        self.Idle_R = load_image('Mario_R.png')
        self.Idle_L = load_image('Mario_L.png')
        self.Walk_R = load_image('Mario_WalkR.png')
        self.Walk_L = load_image('Mario_WalkL.png')
        self.Jump_R = load_image('Mario_JumpR.png')
        self.Jump_L = load_image('Mario_JumpL.png')

    def update(self):
        pass

    def draw(self):
        if Check_Dir == 1:
            if Check_Move == 0:
                self.Idle_R.draw(self.x, self.y)
            elif Check_Move == 1:
                self.Idle_R.clip_draw(self.frame * 32, 0, 32, 32, self.x, self.y)
            elif Check_Move == -1:
                self.Jump_R.draw(self.x, self.y)

        elif Check_Dir == -1:
            if Check_Move == 0:
                self.Idle_L.draw(self.x, self.y)
            elif Check_Move == 1:
                self.Walk_L.clip_draw(self.frame * 32, 0, 32, 32, self.x, self.y)
            elif Check_Move == -1:
                self.Jump_L.draw(self.x, self.y)

def handle_events():
    global Check_Dir, Check_Move
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
            mario.x = mario.x + mario.Speed
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            Check_Dir = -1
            Check_Move = 1
            mario.x = mario.x - mario.Speed


mario = None
running = None

# 마리오의 방향을 확인하기 위한 변수 오른쪽일 경우 1, 왼쪽일 경우 -1
Check_Dir = 1
# 마리오의 행동을 확인하기 위한 변수 아이들일 경우 0, 이동할 경우 1, 점프할 경우 -1
Check_Move = 0



open_canvas()


def enter():
    global mario, running

    mario = Mario()
    # grass = Grass()
    running = True


def exit():
    global mario

    del mario


def update():
    mario.update()


def draw():
    clear_canvas()
    mario.draw()
    update_canvas()


open_canvas()

while running:
    handle_events()
    update()
    draw()
exit()

# finalization code
close_canvas()
