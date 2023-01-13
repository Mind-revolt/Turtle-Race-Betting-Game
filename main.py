from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
# set up method allows to choose the height and width of window
# keyword arguments are the name of the parameter, it's readable so good
screen.setup(width=500, height=400)
# next is a pop-up window, use textinput method for string, numinput for number
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')


# get the turtle to the left of the screen, use goto for that
# home coordinates (middle of the screen) are always (0, 0)
# if height is 400 then from the home coordinates to the top it will be 200 and to the bottom -200
# by default width is x, height is y
# x = 120
# y = 100

# the starting point of the race  is width=-250 and height whatever
# to see the turtle move it a bit towards right.

colors = ['red', 'orange', 'yellow', 'blue', 'purple', 'green']

all_turtles = []
x = -150
i = 0
for turtle in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-240, y=x)
    all_turtles.append(new_turtle)
    x += 50
    i += 1

# set finish line (finish line coordinate - half of the turtle size
# to check for a single coordinate use xcor() method

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            is_race_on = False
            if user_bet == winner_color:
                print(f"You've won! Turtle {winner_color} was first to the finish line")
            else:
                print(f"You've lost. Color {winner_color} was first to the finish line")
        random_number = random.randint(0, 10)
        turtle.forward(random_number)






screen.exitonclick()
