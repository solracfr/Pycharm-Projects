from turtle import Turtle, Screen
import random as rand

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)  # keyword arguments make it much easier to understand what your args are doing
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_starting_position = -100

for turtle_index in range(0, 6):  # how to control each individual turtle when they're all allocated to "tim"?

    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_starting_position)
    all_turtles.append(new_turtle)

    y_starting_position += 30

if user_bet:  # returns True so long as user_bet is not None
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()  # get winning turtle color
            if winning_color == user_bet:
                print("congratulations, you won!")
            else:
                print("hahahah lmaoooo dude")

        random_distance = rand.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
