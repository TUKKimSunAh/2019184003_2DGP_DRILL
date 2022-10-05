import turtle


def up_turtle():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()


def down_turtle():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def left_turtle():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def right_turtle():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()


def restart():
    turtle.reset()

turtle.shape('turtle')


turtle.onkey(up_turtle,'w')
turtle.onkey(down_turtle,'s')
turtle.onkey(left_turtle,'a')
turtle.onkey(right_turtle,'d')
turtle.onkey(restart,'Escape')
turtle.listen()
