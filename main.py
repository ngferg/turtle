from prettytable import PrettyTable
from turtle import _Screen, Turtle, Screen
import random

def timmy_inbounds(screen: _Screen, timmy: Turtle) -> bool:
    t_x = timmy.xcor()
    t_y = timmy.ycor()
    s_x = float(screen.canvwidth+3)
    s_y = float(screen.canvheight)

    return t_x < s_x and t_x > s_x * -1 and t_y < s_y and t_y > s_y * -1

border = Turtle()
timmy = Turtle()
table = PrettyTable()
table.add_column('x', [])
table.add_column('y', [])

timmy.shape('turtle')
border.shape('square')
border.shapesize(30, 30)
border.color('black')
timmy.color('blue')

screen = Screen()
print(f'{screen.canvheight}, {screen.canvwidth}')
screen.screensize(300, 300)

timmy.left(random.randint(0,360))
timmy.forward(1)

while timmy_inbounds(screen, timmy):
    timmy.forward(1)
    table.add_row([timmy.xcor(), timmy.ycor()])
    timmy.left(random.randint(-10, 10))
                  


print(table)
