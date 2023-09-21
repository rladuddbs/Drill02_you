from pico2d import *


def run_circle():
    print('CIRCLE')
    pass


def run_rectangle():
    print('RECTANGLE')
    pass


open_canvas()

character = load_image("character.png")
grass = load_image("grass.png")



while(True):
    run_circle()
    run_rectangle()
    grass.draw_now(400,30)
    character.draw_now(400,90)
    delay(1)

close_canvas()
