from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]    #---> constant
MOVE_DIST=20  #so we can change however we want.
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.snks=[]
        self.create_snk()
        #self.create() in __init__ so we dont have to create a snake each time


    def create_snk(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def add_segment(self,pos):
        new_snk = Turtle("square")
        new_snk.color("white")
        self.snks.append(new_snk)
        new_snk.penup()
        new_snk.goto(pos)

    def extend(self):
        self.add_segment(self.snks[-1].position())


    def move(self):
        for snk_num in range(len(self.snks) - 1, 0, -1):
            new_x = self.snks[snk_num - 1].xcor()
            new_y = self.snks[snk_num - 1].ycor()
            self.snks[snk_num].goto(new_x, new_y)
        self.snks[0].forward(MOVE_DIST)


    def up(self):
        if self.snks[0].heading()!=DOWN:
            self.snks[0].setheading(UP)
    def down(self):
        if self.snks[0].heading()!=UP:
            self.snks[0].setheading(DOWN)
    def right(self):
        if self.snks[0].heading()!=LEFT:
            self.snks[0].setheading(RIGHT)
    def left(self):
        if self.snks[0].heading()!=RIGHT:
            self.snks[0].setheading(LEFT)

    