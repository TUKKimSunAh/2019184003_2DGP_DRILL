from pico2d import *

import Game_Framework
import Play_Stage1
import Title_State


image = None

def enter():
    global image
    image = load_image('manual.png')

def exit():
    global image
    del image
    pass

def update():
    Play_Stage1.update()
    pass

def draw():
    clear_canvas()
    Play_Stage1.draw_world()
    image.draw(400, 500)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key== SDLK_m:
                    Game_Framework.pop_state()