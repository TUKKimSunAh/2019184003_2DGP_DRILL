from pico2d import *
import Game_Framework
import Game_World
import Logo_State
import Manual_State

from Mario import Mario
from Goomba import Goomba
from Long_Block import Long_Block
from Bricks import Bricks
from Pipe1 import Pipe1
from Iron import Iron
from QBox1 import QBox1
from QBox2 import QBox2
from QBox3 import QBox3
from QDie import QDie
from Coin import Coin


class Stage1:
    def __init__(self):
        self.width, self.height = 4000, 600
        self.x, self.y = 2000, 300
        self.Stage_1 = load_image('Map_Stage1.png')

    def update(self):
        pass

    def draw(self):
        self.Stage_1.draw(self.x - 180, self.y)


def handle_events():
    events = get_events()

    for event in events:
        mario.handle_events(event)

        if event.type == SDL_QUIT:
            Game_Framework.quit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                Game_Framework.change_state(Logo_State)

            if event.key == SDLK_m:
                Game_Framework.push_state(Manual_State)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False
    return True


def Check_Collision_Rect(Dest, Src):
    fWidth = abs(Dest.x - Src.x)
    fHeight = abs(Dest.y - Src.y)

    fCX = (Dest.width + Src.width) * 0.5
    fCY = (Dest.height + Src.height) * 0.5

    if (fCX > fWidth) and (fCY > fHeight):
        pWidth = fCX - fWidth
        pHeight = fCY - fHeight

        return 'True', pWidth, pHeight

    return 'False', fWidth, fHeight


stage1 = None
mario = None
long_block = None
bricks = None
pipe1 = None
goomba = None
qbox1 = None
coin = None


def enter():
    global stage1, mario, long_block, bricks, pipe1, goomba, qbox1, coin

    mario = Mario()
    stage1 = Stage1()
    bricks = Bricks(350, 110)
    pipe1 = Pipe1(170, 120)
    goomba = Goomba(100, 200)
    long_block = Long_Block(100, 40)
    qbox1 = QBox1(110, 200)
    coin = Coin(110, 197)

    Game_World.Add_Object(long_block, 3)
    Game_World.Add_Object(mario, 2)
    Game_World.Add_Object(bricks, 1)
    Game_World.Add_Object(pipe1, 0)
    Game_World.Add_Object(goomba, 4)
    Game_World.Add_Object(qbox1, 6)
    Game_World.Add_Object(coin, 5)


def exit():
    Game_World.Clear()


def update():
    stage1.update()

    for game_object in Game_World.All_Objects():
        game_object.update()

    if collide(mario, long_block):
        mario.Force = 0

    if collide(goomba, long_block):
        goomba.Force = 0

    bGoombaCollision, fWidth, fHeight = Check_Collision_Rect(goomba, bricks)
    if bGoombaCollision == 'True':
        goomba.DirCheck *= -1

    bGoombaCollision, fWidth, fHeight = Check_Collision_Rect(goomba, pipe1)
    if bGoombaCollision == 'True':
        goomba.DirCheck *= -1

    bBricksCollision, fWidth, fHeight = Check_Collision_Rect(mario, bricks)

    if bBricksCollision == 'True':
        if fWidth > fHeight:
            if mario.y < bricks.y:
                print(fHeight)
                mario.y = mario.y - fHeight
            else:
                mario.y = mario.y + fHeight

        else:
            if mario.x < bricks.x:
                mario.x = mario.x - fWidth
            else:
                print(fWidth)
                mario.x = mario.x + fWidth

    bPipe1Collision, fWidth, fHeight = Check_Collision_Rect(mario, pipe1)

    if bPipe1Collision == 'True':
        if fWidth > fHeight:
            if mario.y < bricks.y:
                print(fHeight)
                mario.y = mario.y - fHeight
            else:
                mario.y = mario.y + fHeight

        else:
            if mario.x < bricks.x:
                mario.x = mario.x - fWidth
            else:
                print(fWidth)
                mario.x = mario.x + fWidth

    if bPipe1Collision == 'True':
        if fWidth > fHeight:
            if mario.y < bricks.y:
                print(fHeight)
                mario.y = mario.y - fHeight
            else:
                mario.y = mario.y + fHeight

        else:
            if mario.x < bricks.x:
                mario.x = mario.x - fWidth
            else:
                print(fWidth)
                mario.x = mario.x + fWidth

    bPipe1Collision, fWidth, fHeight = Check_Collision_Rect(mario, pipe1)

    if bPipe1Collision == 'True':
        if fWidth > fHeight:
            if mario.y < bricks.y:
                print(fHeight)
                mario.y = mario.y - fHeight
            else:
                mario.y = mario.y + fHeight

        else:
            if mario.x < bricks.x:
                mario.x = mario.x - fWidth
            else:
                print(fWidth)
                mario.x = mario.x + fWidth

    bQbox1Collision, fWidth, fHeight = Check_Collision_Rect(mario, qbox1)

    if bQbox1Collision == 'True':
        if fWidth > fHeight:
            if mario.y < qbox1.y:
                temp = fHeight
                mario.y = mario.y - fHeight
                print(qbox1.CheckState)
                qbox1.CheckState += 1
            else:
                mario.y = mario.y + fHeight

        else:
            if mario.x < bricks.x:
                mario.x = mario.x - fWidth
            else:
                print(fWidth)
                mario.x = mario.x + fWidth

    bCoinCollision, fWidth, fHeight = Check_Collision_Rect(mario, coin)

    if bCoinCollision == 'True':
        if fWidth > fHeight:
            if mario.y < coin.y:
                print('와부딪혓서요~')
                coin.y = coin.y + (coin.height/2)*3
            else:
                mario.y = mario.y + fHeight

        else:
            if mario.x < bricks.x:
                mario.x = mario.x - fWidth
            else:
                print(fWidth)
                mario.x = mario.x + fWidth


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    stage1.draw()
    for game_object in Game_World.All_Objects():
        game_object.draw()


def pause():
    pass


def resume():
    pass


def pause():
    pass


def resume():
    pass


def test_self():
    import Play_Stage1

    pico2d.open_canvas()
    Game_Framework.run(Play_Stage1)
    pico2d.clear_canvas()


if __name__ == '__main__':
    test_self()
