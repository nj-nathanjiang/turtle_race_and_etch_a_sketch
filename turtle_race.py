import random
import turtle as t

screen = t.Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter the color.").lower()
is_race_on = False

timmy_blue = t.Turtle()
blue_reach_end = False
timmy_blue.color("blue")
timmy_blue.shape("turtle")
timmy_blue.penup()
timmy_blue.goto(x=-225, y=-100)

timmy_red = t.Turtle()
red_reach_end = False
timmy_red.color("red")
timmy_red.shape("turtle")
timmy_red.penup()
timmy_red.goto(x=-225, y=-70)

timmy_orange = t.Turtle()
orange_reach_end = False
timmy_orange.color("orange")
timmy_orange.shape("turtle")
timmy_orange.penup()
timmy_orange.goto(x=-225, y=-40)

timmy_yellow = t.Turtle()
yellow_reach_end = False
timmy_yellow.color("yellow")
timmy_yellow.shape("turtle")
timmy_yellow.penup()
timmy_yellow.goto(x=-225, y=-10)

timmy_green = t.Turtle()
green_reach_end = False
timmy_green.color("dark green")
timmy_green.shape("turtle")
timmy_green.penup()
timmy_green.goto(x=-225, y=20)

timmy_purple = t.Turtle()
purple_reach_end = False
timmy_purple.color("purple")
timmy_purple.shape("turtle")
timmy_purple.penup()
timmy_purple.goto(x=-225, y=50)

list_of_turtles_strings = ["timmy_purple", "timmy_orange", "timmy_green", "timmy_red", "timmy_blue", "timmy_yellow"]
list_of_turtles = [timmy_purple, timmy_orange, timmy_green, timmy_red, timmy_blue, timmy_yellow]
finished_race = []


def move_forward_random(turtle):
    random_number = random.randint(0, 10)
    turtle.forward(random_number)


if user_bet:
    is_race_on = True

while is_race_on:
    move_forward_random(timmy_purple)
    move_forward_random(timmy_green)
    move_forward_random(timmy_red)
    move_forward_random(timmy_yellow)
    move_forward_random(timmy_blue)
    move_forward_random(timmy_orange)
    turtle_on = 0
    for any_turtle in list_of_turtles:
        if any_turtle.xcor() >= 225:
            is_race_on = False
            finished_race.append(list_of_turtles_strings[turtle_on])
        turtle_on += 1

for winner in finished_race:
    print(f"{winner} won!")
    
if user_bet in finished_race:
    print("You were correct!")
else:
    print("You guessed wrong. Better luck next time.")

screen.exitonclick()
