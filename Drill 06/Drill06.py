from pico2d import *
import math

open_canvas()


grass=load_image('grass.png')
character=load_image('character.png')


case=1
char_x=0
char_y=90

character.draw_now(400,90)
grass.draw_now(400,30)

if (case==1):
    while(char_x<700):
        clear_canvas_now()
        grass.draw_now(400,30)

        if(char_y==90):
            character.draw_now(char_x,90)
            char_x=char_x+2
            delay(0.01)

            if(

        elif char_y==500:
            character.draw_now(char_x,90)
            char_x=char_x+2
            delay(0.01)

    while(char_y<100):
        clear_canvas_now()
        grass.draw_now(400,30)

        if(char_x<500):
            character.draw_now(700,char_y)
            char_x=char_x+2
            delay(0.01)

        elif char_y>=500:
            character.draw_now(char_x,90)
            char_x=char_x+2
            delay(0.01)

        
