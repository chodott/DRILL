from pico2d import *
import math
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x=0
y=90
r = 250
rad = 270
while -1:
    # 캐릭터 사각 운동
    while(x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x+2
        delay(0.01)
    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y+2
        delay(0.01)
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x -= 2
        delay(0.01)
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y -= 2
        delay(0.01)
    while(x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x+2
        delay(0.01)
    # 캐릭터 원 운동
    
close_canvas()
