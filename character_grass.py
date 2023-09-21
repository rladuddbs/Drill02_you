from pico2d import *

import math



cx, cy = 400, 300

def render_frame(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.001)
    update_canvas()

def run_circle():
    print('CIRCLE')
    r = 200
    for deg in range(-90,270,1):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        render_frame(x,y)


def run_rectangle():
    print('RECTANGLE')
    x = 400
    # bottom line
    for x in range(400, 750 + 1, 1): 
        render_frame(x,90)

    # right line
    for y in range(90,570,1):
        render_frame(750 + 1, y)
    
    # top line
    for x in range(750, 50, -1): 
        render_frame(x,550)

    # left line
    for y in range(570,90,-1):
        render_frame(20, y)

    # bottom2 line
    for x in range(0, 400, 1): 
        render_frame(x,90)
        
open_canvas()

character = load_image("character.png")
grass = load_image("grass.png")



while(True):
    run_circle()
    run_rectangle()
    
    
close_canvas()
