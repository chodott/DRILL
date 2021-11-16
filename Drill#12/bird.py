#새의 크기 = 100x100 픽셀, 3x3 미터
#새의 속도 = 60km/h 참새의 최대 비행속도이다
#날개짓 속도 = 초당 2회

import random
from pico2d import *
import game_world
from random import *
import game_framework

#fly speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FLY_SPEED_KMPH = 60.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y, = randint(200,1000), randint(0,600)
        self.frame = 0
        self.rand = randint(0,1)
        self.dir = 0
        if self.rand ==0: self.dir = -1
        else: self.dir = 1


    def draw(self):
        self.image.clip_draw(100*(int)(self.frame),0,100,100,self.x,self.y)
        # fill here for draw

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += game_framework.frame_time * FLY_SPEED_PPS * self.dir
        if self.x - 50 <= 0 or self.x + 50 >= 1600:
            self.dir *= -1
