from pico2d import *

import math

cx, cy = 400, 300


def run_circle():
    print('CIRCLE')
    r = 200
    for deg in range(0,270,5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.05)


def run_rectangle():
    print('RECTANGLE')
    for x in range(50,750+1,5): 
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        delay(0.05)
    
open_canvas()

character = load_image("character.png")
grass = load_image("grass.png")



while(True):
    run_circle()
    run_rectangle()
    break
    
close_canvas()
