from pico2d import *
from random import *


open_canvas()
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x = 800 // 2
y = 600 // 2
handx, handy = x,y
frame = 0
stop = 1
slope = 0
dir = 0 # -1 left +1 right

while running:
    clear_canvas()
    hand.draw(handx,handy)
    if x>handx: character.clip_draw(frame * 100, 0, 100, 100, x, y)
    else: character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    if stop :
        handx = randint(1,800)
        handy = randint(1,600)
        slope = (y-handy)/(x-handx)
        stop = 0
    else :
        if x<handx :
            x+=1
            y += slope * 1
        elif x>=handx :
            x-=1
            y += slope * -1
        if(x<=handx+1 and x >= handx-1 and y >= handy-1 and y <= handy+1): stop = 1
        
    frame = (frame + 1) % 8
    
    delay(0.01)
    pass

close_canvas()

