from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
screen = Screen()

def move(steps: int):
    tim.forward(steps)

def turn(degrees: int):
    tim.left(degrees)

screen.listen()
screen.onkey(key='Up', fun=lambda: move(10))
screen.onkey(key='Down', fun=lambda: move(-10))
screen.onkey(key='Escape', fun=screen.bye)
screen.onkey(key='Left', fun=lambda: turn(10))
screen.onkey(key='Right', fun=lambda: turn(-10))
screen.onkey(key='c', fun=screen.reset)

screen.mainloop()
