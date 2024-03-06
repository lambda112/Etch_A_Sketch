import turtle as t

pen = t.Turtle()
screen = t.Screen()

def move():
    pen.forward(2)

screen.listen()
screen.onkeypress(key = "w", fun=move)

screen.exitonclick()