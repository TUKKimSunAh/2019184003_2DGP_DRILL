from pico2d import *

import game_framework
import play_state
import title_state


image = None
count = 1

def enter():
    global image
    image = load_image('item_select.png')

def exit():
    global image
    del image
    pass

def update():
    play_state.update()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    global count

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_0:
                    play_state.boy.item = None
                    game_framework.pop_state()
                case pico2d.SDLK_1:
                    play_state.boy.item = 'Ball'
                    game_framework.pop_state()
                case pico2d.SDLK_2:
                    play_state.boy.item = 'BigBall'
                    game_framework.pop_state()
                case pico2d.SDLK_j:
                    if count == 1:
                        game_framework.pop_state()
                        break
                    count -= 1
                    play_state.initTeam(count)
                    game_framework.pop_state()

                case pico2d.SDLK_k:
                    count += 1
                    play_state.initTeam(count)
                    game_framework.pop_state()




