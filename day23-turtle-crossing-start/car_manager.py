from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_cars(self):
        if random.randint(1, 6) == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.penup()
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
        self.cars = [car for car in self.cars if car.xcor() > -320]

    def user_hit(self, user):
        user_y_cor = user.ycor()
        for car in self.cars:
            abs_y = abs(user_y_cor - car.ycor())
            abs_x = abs(car.xcor())
            if abs_y < 20 and abs_x < 30:
                return True
        return False
