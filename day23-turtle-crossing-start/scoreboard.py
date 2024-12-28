from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-280, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.level = 1

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def print_game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)
