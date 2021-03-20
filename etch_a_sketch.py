import turtle as t

timmy = t.Turtle()
screen = t.Screen()
timmy.shape("turtle")
timmy.color("dark green")


def go_forwards():
    timmy.forward(5)


def turn_left():
    new_heading = timmy.heading() + 5
    timmy.setheading(new_heading)


def turn_right():
    new_heading = timmy.heading() -5
    timmy.setheading(new_heading)


def go_backwards():
    timmy.back(5)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(key="Up", fun=go_forwards)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Down", fun=go_backwards)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
