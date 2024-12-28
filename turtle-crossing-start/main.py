import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

speed = 0.2

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    screen.update()
    score_board.update_scoreboard()
    time.sleep(speed)

    car_manager.create_cars()
    car_manager.move()

    if car_manager.user_hit(player):
        game_is_on = False
        score_board.print_game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        speed /= 2
        score_board.level_up()

screen.exitonclick()

