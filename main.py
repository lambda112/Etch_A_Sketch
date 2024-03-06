import turtle as t

pen = t.Turtle()
screen = t.Screen()

def move():
    pen.forward(10)

def turn_left():
    pen.left(10)

def turn_right():
    pen.right(10)

def turn_back():
    pen.back(10)

def clear_screen():
    pen.reset()


screen.listen()
screen.onkeypress(key = "w", fun=move)
screen.onkeypress(key = "a", fun=turn_left)
screen.onkeypress(key = "d", fun=turn_right)
screen.onkeypress(key = "s", fun=turn_back)
screen.onkeypress(key = "c", fun=clear_screen)
screen.exitonclick()