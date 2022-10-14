from pico2d import *

import Game_Framework
import Title_State


image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('logo.png')
    pass

def exit():
    global image
    del image
    pass

def update():
    global logo_time

    if logo_time > 1.0:
        logo_time = 0
        Game_Framework.change_state(Title_State)
    delay(0.01)
    logo_time += 0.01
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass

def handle_events():
    events = get_events()





