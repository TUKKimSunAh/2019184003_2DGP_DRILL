from pico2d import *
TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    global dirLR
    global dirUD
    global dirBack

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirLR += 1
                dirBack = 1
            elif event.key == SDLK_LEFT:
                dirLR -= 1
                dirBack = -1
            elif event.key == SDLK_UP:
                dirUD += 1
            elif event.key == SDLK_DOWN:
                dirUD -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirLR -= 1
            elif event.key == SDLK_LEFT:
                dirLR += 1
            elif event.key == SDLK_UP:
                dirUD -= 1
            elif event.key == SDLK_DOWN:
                dirUD += 1


def Do_not_Move():
    global x, y

    if x >= TUK_WIDTH:
        x = TUK_WIDTH-50
    if y >= TUK_HEIGHT:
        y = TUK_HEIGHT-45
    if x <= 0:
        x = 50
    if y <= 0:
        y = 45

open_canvas()
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
dirLR = 0
dirUD = 0
dirBack = 1


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    Do_not_Move()

    if dirLR == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif dirLR == -1:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    elif dirUD == +1:
        if dirBack == 1:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif dirBack == -1:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
    elif dirUD == -1:
        if dirBack == 1:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif dirBack == -1:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
    elif dirLR == 0:
        if dirBack == 1:
            character.clip_draw(100, 100 * 3, 100, 100, x, y)
        elif dirBack == -1:
            character.clip_draw(100, 100 * 2, 100, 100, x, y)


    update_canvas()



    handle_events()
    frame = (frame + 1) % 8
    x += dirLR * 5
    y += dirUD * 5
    delay(0.01)

close_canvas()

