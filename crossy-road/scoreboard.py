from turtle import Turtle

FONT = ("Courier", 24, "normal")
LOCATION = (-200, 220)
CENTER = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(LOCATION)
        self.update_score()

    # update score
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align=CENTER, font=FONT)

    # increase the score by one and update the scoreboard
    def increase_score(self):
        self.level += 1
        self.update_score()

    # make a Game Over screen
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over loser :(", align=CENTER, font=FONT)

