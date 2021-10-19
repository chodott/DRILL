from pico2d import *
import random
# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)
    pass

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100,500),90
        self.frame = random.randint(0,8)

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

    def update(self): #소년의 행위 구현
        self.x +=5
        self.frame = (self.frame + 1) % 8

    pass


class BigBall:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0,800), 599
        self.speed = random.randint(10,20)

    def draw(self):
        self.image.clip_draw(0,0,41,41,self.x,self.y)

    def update(self):
        self.y -= self.speed
        if self.y < 70:
            self.y = 70

class SmallBall:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0,800), 599
        self.speed = random.randint(10,20)

    def draw(self):
        self.image.clip_draw(0,0,21,21,self.x,self.y)

    def update(self):
        self.y -= self.speed
        if self.y < 60:
            self.y = 60

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass()
# boy = Boy()
team = [Boy() for i in range(11)]
bigBalls = [BigBall() for i in range(11)]
smallBalls = [SmallBall() for i in range(11)]


running = True
# game main loop code
while running:

    handle_events()

    #Game logic
    for boy in team:
        boy.update()
    for ball in bigBalls:
        ball.update()
    for ball in smallBalls:
        ball.update()


    #game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in bigBalls:
        ball.draw()
    for ball in smallBalls:
        ball.draw()
    update_canvas()

    delay(0.05)

# finalization code