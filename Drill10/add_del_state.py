from pico2d import *

import game_framework
import play_state
import title_state


image = None
boy_plus = 1

def enter():
    global image
    image = load_image('add_delete_boy.png')

def exit():
    global image
    del image
    pass

def update():
    # play_state.update()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    global boy_plus
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_k:
                    boy_plus += 1
                    game_framework.pop_state()
                case pico2d.SDLK_j:
                    boy_plus -= 1
                    game_framework.pop_state()



