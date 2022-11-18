from pico2d import *
import Game_World

# Stage1 맵 크기
Stage1_WIDTH, Stage1_HEIGHT = 4000, 600

# 게임 플레이 화면
WIN_WIDTH, WIN_HEIGHT = 800, 600

# 마리오의 방향을 확인하기 위한 변수 | 오른쪽일 경우 1, 왼쪽일 경우 -1
Check_Dir = 1
# 마리오의 행동을 확인하기 위한 변수 | 아이들일 경우 0, 오른쪽일 경우 1, 왼쪽일 경우 -1
Check_Move = 0
# 마리오의 점푸를 확인하기 위한 변수 | 아이들일 경우 0, 오른쪽 점프할 경우 1, 왼쪽 점프할 경우 -1
Check_Jump = 1
# 마리오 점프 여부 | True, False로 판단
bJump = False


class Mario:
    global Check_Dir, Check_Move, bJump, Check_Jump

    def __init__(self):
        self.x, self.y = 20, 300
        self.width, self.height = 32, 32
        self.Speed = 0.5
        self.frame = 0
        self.Force = 0
        self.Gravity = 0.09

        self.Idle_R = load_image('Mario_R.png')
        self.Idle_L = load_image('Mario_L.png')
        self.Walk_R = load_image('Mario_WalkR.png')
        self.Walk_L = load_image('Mario_WalkL.png')
        self.Jump_R = load_image('Mario_JumpR.png')
        self.Jump_L = load_image('Mario_JumpL.png')

    def update(self):
        self.Force += 0.01
        self.Set_Gravity()

        if Check_Move == 1:
            self.frame = (self.frame + 1) % 3
            self.x = self.x + self.Speed

        elif Check_Move == -1:
            self.frame = (self.frame + 1) % 3
            self.x = self.x - self.Speed

        elif bJump:
            self.y += 3.5
            self.Force += 0.03

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

    def Set_Gravity(self):
        self.y += self.Force
        self.Force -= self.Gravity

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

    def handle_events(self, event):
        global Check_Dir, Check_Move, bJump, Check_Jump

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_d:
                Check_Dir = 1
                Check_Move = 1

            if event.key == SDLK_a:
                Check_Dir = -1
                Check_Move = -1

            if event.key == SDLK_w:
                if Check_Dir == 1:
                    Check_Jump = 1
                elif Check_Dir == -1:
                    Check_Jump = -1

                bJump = True

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a or event.key == SDLK_d:
                Check_Move = 0

            if event.key == SDLK_w:
                bJump = False
                Check_Jump = 0
