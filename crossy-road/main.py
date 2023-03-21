import time
import random as r
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

HITBOX_DISTANCE = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()
scoreboard = Scoreboard()

player = Player()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if r.randint(1, 6) % 6 == 0:  # this is purely arbitrary and it controls the rate that cars spawn
        car_manager.create_car()

    car_manager.move_cars()

    for car in car_manager.cars:
        if player.distance(car) < HITBOX_DISTANCE:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.reset()
        scoreboard.increase_score()

screen.exitonclick()
