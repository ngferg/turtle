import turtle
import random

def random_color() -> dict[str, float]:
    return {
        "r": random.randint(0, 255), 
        "g": random.randint(0, 255), 
        "b": random.randint(0, 255)
    }

timmy = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
timmy.speed(0)

timmy.shape('turtle')
rgb = random_color()
timmy.color(rgb['r'], rgb['g'], rgb['b'])


# dash
# for _ in range(0,10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# shapes
# for sides in range(3, 10):
#     rgb = random_color()
#     timmy.color(rgb['r'], rgb['g'], rgb['b'])
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(360/sides)

# random walk
# running = True
# timmy.pensize(10)
# while running:
#     direction = random.randint(0, 3)
#     timmy.left(90 * direction)
#     timmy.forward(25)
#     rgb = random_color()
#     timmy.color(rgb['r'], rgb['g'], rgb['b'])

timmy.pensize(5)

def move():
    rgb = random_color()
    timmy.color(rgb['r'], rgb['g'], rgb['b'])
    timmy.forward(25)
    screen.update()

def up():
    timmy.setheading(90)
    move()

def left():
    timmy.setheading(180)
    move()

def right():
    timmy.setheading(0)
    move()

def down():
    timmy.setheading(270)
    move()

def home():
    timmy.penup()
    timmy.home()
    timmy.pendown()
    screen.update()

screen.onkeypress(key='w', fun=up)
screen.onkeypress(key='a', fun=left)
screen.onkeypress(key='d', fun=right)
screen.onkeypress(key='s', fun=down)
screen.onkeypress(key='h', fun=home)
screen.onkeypress(key='q', fun=screen.bye)

print(timmy.heading())

screen.tracer(False)
screen.listen()
screen.update()
screen.mainloop()
