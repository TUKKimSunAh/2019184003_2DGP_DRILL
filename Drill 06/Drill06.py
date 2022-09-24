from pico2d import *
import math

global case
case =1

def draw_square(char_x, char_y):

    global case 
    if char_x==0 and char_y==90:
        while(char_x<700):
            clear_canvas_now()
            character.draw_now(char_x,90)
            grass.draw_now(400,30)
            char_x=char_x+2
            delay(0.01)
            
    if char_x==700 and char_y==90:
        while(char_y<500):
            clear_canvas_now()
            character.draw_now(700, char_y)
            grass.draw_now(400,30)
            char_y=char_y+2
            delay(0.01)

    if char_x==700 and char_y==500:
         while(char_x>100):
            clear_canvas_now()
            character.draw_now(char_x, 500)
            grass.draw_now(400,30)
            char_x=char_x-2
            delay(0.01)

    if char_x==100 and char_y==500:
        
        while(char_y>90):
            clear_canvas_now()
            character.draw_now(100, char_y)
            grass.draw_now(400,30)
            char_y=char_y-2
            delay(0.01)
        case=2

def draw_circle(char_x, char_y):

open_canvas()

char_x=0
char_y=90

grass=load_image('grass.png')
character=load_image('character.png')


character.draw_now(0,90)
grass.draw_now(400,30)

if case==1:
    draw_square(char_x, char_y)

if case==2:
    




        
