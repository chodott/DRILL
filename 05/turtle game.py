import turtle as t

def go_up():
    t.stamp()
    t.setheading(90)
    t.forward(50)

def go_down():
    t.stamp()
    t.setheading(270)
    t.forward(50)

def go_left():
    t.stamp()
    t.setheading(180)
    t.forward(50)

def go_right():
    t.stamp()
    t.setheading(0)
    t.forward(50)

def go_escape():
    t.reset()

t.shape("turtle")

t.onkeypress(go_up,"w")
t.onkeypress(go_down,"s")
t.onkeypress(go_left,"a")
t.onkeypress(go_right,"d")
t.onkeypress(go_escape,"Escape")

t.listen()
                             
