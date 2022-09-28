from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('Player.png')

def Right_Player():
    frame=0
    for player_x in range(100, 700,5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 63, 0, 63, 63, player_x, 65)
        frame = (frame + 1) % 9
        update_canvas()
        delay(0.01)
        get_events()

def Left_Player():
    frame=0
    for player_x in range(700,100,-5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 63, 130, 63, 63, player_x, 65)
        frame = (frame + 1) % 10
        update_canvas()
        delay(0.01)
        get_events()


def WhatRight_Player():
    frame=0
    for player_x in range(100,600,5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 63, 260, 63, 63, player_x, 65)
        frame = (frame + 1) % 8
        update_canvas()
        delay(0.01)
        get_events()



def WhatLeft_Player():
    frame=0
    for player_x in range(600,100,-5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 63, 390, 63, 63, player_x, 65)
        frame = (frame + 1) % 8
        update_canvas()
        delay(0.01)
        get_events()




while(True):
    Right_Player()
    Left_Player()
    WhatRight_Player()
    WhatLeft_Player()

