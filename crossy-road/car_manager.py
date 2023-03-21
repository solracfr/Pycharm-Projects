from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_CARS = 30


class CarManager:
    def __init__(self):
        self.cars = []
        self.x_step = STARTING_MOVE_DISTANCE

    # create all the cars we'll use in the game
    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(r.choice(COLORS))
        new_car.goto(300, r.randint(-220, 280))

        self.cars.append(new_car)

    # move cars towards the left
    def move_cars(self):
        for car in self.cars:
            car.backward(self.x_step)

    # increment car speed
    def increase_car_speed(self):
        self.x_step += MOVE_INCREMENT

