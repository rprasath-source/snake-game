from turtle import Turtle
from snake import Snake
from food import Food

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"score: {self.score}",align="center",font=("Arial",14,"normal"))
        self.goto(-130, 20)
        self.write("PRESS 'space' TO START", font=("Arial", 20, "normal"))
        self.game_is_on=False
        self.hideturtle()

    def game_start(self):
        self.clear()
        self.game_is_on=True


    def scr_update(self):
        self.score+=1
        self.clear()
        self.goto(0,270)
        self.write(f"score: {self.score}", align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.hideturtle()
        self.goto(-80,0)
        self.write("GAME OVER!",font=("Arial",24,"normal"))
        self.goto(-35,40)
        self.write(f"SCORE:{self.score}",font=("Arial",14,"normal"))
