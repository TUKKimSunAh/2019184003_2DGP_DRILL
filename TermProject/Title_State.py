from pico2d import *

import Game_Framework
import Play_Stage1

image = None

def enter():
    global image
    image = load_image('Title.png')
    pass

def exit():
    global image
    del image
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            Game_Framework.change_state(Play_Stage1)
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






