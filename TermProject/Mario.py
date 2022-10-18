from pico2d import *

# Stage1 맵 크기
Stage1_WIDTH, Stage1_HEIGHT = 4000, 600

# 게임 플레이 화면
WIN_WIDTH, WIN_HEIGHT = 800, 600


#키보드나 마우스 관련 이벤트들 관리 함수
def Handle_Events():
    global Game_Wait
    global Game_Play
    global Program_Run
    global Player_x, Player_y
    global Player_Speed

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            Program_Run = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Program_Run = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            Player_x = Player_x + Player_Speed
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            Player_x = Player_x - Player_Speed


def Scroll():
    global offsetX
    global scrollX
    global Player_x, Player_y
    global Player_Speed

    if (offsetX + 200) < Player_x:
        scrollX -= Player_Speed*2
        offsetX += Player_Speed

    if (offsetX + 200) > Player_x:
        scrollX += Player_Speed*2
        offsetX -= Player_Speed

open_canvas(WIN_WIDTH, WIN_HEIGHT)

#이미지 삽입
Map_Stage1 = load_image('logo.png')
Mario = load_image('Mario.png')


#전역변수들 초기값 설정
Program_Run = True
Game_Wait = False
Game_Play = False

offsetX = WIN_WIDTH//2
scrollX = 0
Player_Speed = 10
Player_x = 10
Player_y = 100


while Program_Run:
    clear_canvas()
    Map_Stage1.draw(10 + scrollX, Stage1_HEIGHT // 2)
    Mario.draw(Player_x, Player_y)
    update_canvas()
    Handle_Events()

close_canvas()




