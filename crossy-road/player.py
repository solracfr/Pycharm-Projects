from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH = 90
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Player(Turtle):
    def __init__(self):
        super().__init__()
        # TODO: set up input for turtle color
        self.shape("turtle")
        self.penup()
        self.setheading(NORTH)
        self.y_step = MOVE_DISTANCE
        self.reset()

    #  Turtle moves up
    def move(self):
        new_y = self.ycor() + self.y_step  # add y_step to current ycor
        self.goto(self.xcor(), new_y)

    # reset player's starting position
    def reset(self):
        self.goto(STARTING_POSITION)
