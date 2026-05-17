# Snake Game

#from turtle import Turtle, Screen
#import time

#screen = Screen()
# Screen setup and Creating a Snake (Step-1)
#screen.setup(width=600, height=600)
#screen.bgcolor("black")
#screen.title("My Snake Game")

#starting_position = [(0,0), (-20, 0), (-40, 0)]

#for position in starting_position:
 #   new_segment = Turtle("square")
 #   new_segment.color("white")
 #   new_segment.goto(position)

# Animating the Snake Segments on Screen(Step-2)

#screen.setup(width=600, height=600)
#screen.bgcolor("black")
#screen.title("My Snake Game")
#screen.tracer(0)

#starting_position = [(0,0), (-20, 0), (-40, 0)]

#segments = []

#for position in starting_position:
 #   new_segment = Turtle("square")
 #   new_segment.goto(position)
 #   segments.append(new_segment)




#game_is_on = True

#while game_is_on:
 #   screen.update()
 #   time.sleep(0.1)
    #(for seg in segments:)
     #   (seg.forward(20))

    #(segments[0].left(90))

    #for seg_num in range(len(segments) - 1, 0, -1):
  #      new_x = segments[seg_num - 1].xcor()
 #       new_y = segments[seg_num - 1].ycor()
 #       segments[seg_num].goto(new_x, new_y)
 #   segments[0].forward(20)
 #   segments[0].left(90)







#screen.exitonclick()

from turtle import Turtle, Screen

import time

import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = (20)

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            


    def add_segment(self, position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))




    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

        




screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()

food = Food()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right, "Right")





game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    





screen.exitonclick()