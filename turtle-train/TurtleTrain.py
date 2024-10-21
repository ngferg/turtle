import turtle
import random


class TurtleTrain(object):
    def __init__(self, turtles: list[turtle.Turtle]):
        self.turtles = turtles
        self.turns = []

    def add_turtle(self):
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
        if self.turns.__len__() > 0:
            self.turns.append({
                'turn_on': self.turns[-1]['turn_on'] + 5,
                'turtle_num': self.turns[-1]['turtle_num'] + 1,
                'heading': self.turns[-1]['heading']

            })

    def move_turtles(self, distance: int):
        i = 0
        for turn in self.turns:
            turn['turn_on'] = turn['turn_on'] - 1
            if turn['turn_on'] == 0:
                self.turtles[turn['turtle_num']].setheading(turn['heading'])
                self.turns = self.turns[1:]
            i += 1
        for turtle in self.turtles:
            turtle.forward(distance)

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
            turn_on = 1
            turtle_num = 0
            for _ in self.turtles[1:]:
                turn_on += 5
                turtle_num += 1
                self.turns.append({
                    'turn_on': turn_on,
                    'turtle_num': turtle_num,
                    'heading': degrees
                })

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        return color

