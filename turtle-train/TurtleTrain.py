import turtle
import random


class TurtleTrain(object):
    def __init__(self, turtles: list[turtle.Turtle]):
        self.turtles = turtles
        self.score = 0

    def add_turtle(self):
        self.score += 1
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.shape('turtle')
        new_turtle.setx(self.get_caboose().xcor())
        new_turtle.sety(self.get_caboose().ycor())

        if int(self.get_caboose().heading()) == 0:
            new_turtle.setx(new_turtle.xcor() - 25)
        elif int(self.get_caboose().heading() == 180):
            new_turtle.setx(new_turtle.xcor() + 25)
        elif int(self.get_caboose().heading()) == 90:
            new_turtle.sety(new_turtle.ycor() - 25)
        elif int(self.get_caboose().heading()) == 270:
            new_turtle.sety(new_turtle.ycor() + 25)
        new_turtle.setheading(self.get_caboose().heading())
        new_turtle.color(self.random_color())
        self.turtles.append(new_turtle)

    def move_turtles(self, distance: int):
        for i in range(len(self.turtles)-1, 0, -1):
            self.turtles[i].goto(self.turtles[i-1].position())
            self.turtles[i].setheading(self.turtles[i-1].heading())
        self.turtles[0].forward(distance)

    def get_conductor(self) -> turtle.Turtle:
        return self.turtles[0]
    
    def get_caboose(self) -> turtle.Turtle:
        return self.turtles[-1]
    
    def intersects(self, other: turtle.Turtle) -> bool:
        in_left = self.get_conductor().xcor() < other.xcor() +  10
        in_right = self.get_conductor().xcor() > other.xcor() - 10
        is_above = self.get_conductor().ycor() > other.ycor() - 10
        is_below = self.get_conductor().ycor() < other.ycor() + 10

        return in_left and in_right and is_above and is_below

    def turn_train(self, degrees: int):
        if degrees != self.get_conductor().heading() + 180 and degrees != self.get_conductor().heading() - 180:  
            self.get_conductor().setheading(degrees)


    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        return color

