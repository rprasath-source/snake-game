from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

turtle=Turtle()
snake=Snake()
food=Food()
screen=Screen()
scoreboard=Scoreboard()

screen.setup(600,600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)


screen.listen()

screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")


screen.onkey(scoreboard.game_start,'space')
game_is_on=True
while game_is_on:
    if scoreboard.game_is_on:
        snake.move()

    time.sleep(0.1)
    if snake.snks[0].distance(food.xcor(), food.ycor()) < 15:
        food.refresh()
        scoreboard.scr_update()
        snake.extend()

    if snake.snks[0].xcor() == 300 or snake.snks[0].xcor() == -300 or snake.snks[0].ycor() == 300 or snake.snks[0].ycor() == -300:
        game_is_on=False
        scoreboard.game_over()

    for snk in snake.snks:
        if snk==snake.snks[0]:
            pass

        elif snake.snks[0].distance(snk) < 10:
            game_is_on=False
            scoreboard.game_over()


    screen.update()






screen.exitonclick()
