import turtle as t

pen = t.Turtle()
screen = t.Screen()

def move():
    pen.forward(5)

def turn_left():
    pen.left(5)

def turn_right():
    pen.right(5)

def turn_back():
    pen.back(5)

screen.listen()
screen.onkeypress(key = "w", fun=move)
screen.onkeypress(key = "a", fun=turn_left)
screen.onkeypress(key = "d", fun=turn_right)
screen.onkeypress(key = "s", fun=turn_back)
screen.exitonclick()