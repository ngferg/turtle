import turtle
import random
import TurtleTrain
from scoreboard import Scoreboard

TICK_RATE = 10

paused = False
screen_size = (600,400)

screen = turtle.Screen()
screen.setup(screen_size[0], screen_size[1], 0, 0)
screen.colormode(255)
screen.tracer(False)
screen.listen()
screen.update()
screen.title('Turtle Train')

conductor = turtle.Turtle()
conductor.shape('turtle')
conductor.penup()

train = TurtleTrain.TurtleTrain([conductor])
train.get_conductor().color(train.random_color())

pellet = turtle.Turtle()
pellet.penup()
pellet.shape('square')
pellet.shapesize(.5, .5)
pellet.setposition(random.randrange(int((-1 * screen_size[0]/2) + 25), int(screen_size[0]/2 - 25), 25), random.randrange(int((-1 * screen_size[1]/2) + 30), int(screen_size[1]/2 - 30), 25))

score_board = Scoreboard(screen_size)

def tick():
    train.move_turtles(25)
    screen.update()
    if not timmy_inbounds(train.get_conductor()):
        game_over()
    if train.intersects(pellet):
        pellet.setposition(random.randrange(int((-1 * screen_size[0]/2) + 25), int(screen_size[0]/2 - 25), 25), random.randrange(int((-1 * screen_size[1]/2) + 30), int(screen_size[1]/2 - 30), 25))
        train.add_turtle()
    for other_turtle in train.turtles[1:]:
        if train.intersects(other_turtle):
            game_over()
    if not paused:
        score_board.write_score(train.score)
        screen.ontimer(tick, int(1000/TICK_RATE))

def face(degrees: int):
    train.turn_train(degrees)

def timmy_inbounds(timmy: turtle.Turtle) -> bool:
    t_x = timmy.xcor()
    t_y = timmy.ycor()
    s_x = float(screen_size[0])/2
    s_y = float(screen_size[1])/2

    return t_x < s_x and t_x > s_x * -1 and t_y < s_y and t_y > s_y * -1

def game_over():
    score_board.write_game_over(train.score)
    screen.exitonclick()
    exit()

def pause():
    global paused
    if paused:
        paused = False
        tick()
    else:
        paused = True
        score_board.write_paused()

screen.onkeypress(game_over, 'q')
screen.onkeypress(lambda: face(90), 'w')
screen.onkeypress(lambda: face(180), 'a')
screen.onkeypress(lambda: face(270), 's')
screen.onkeypress(lambda: face(0), 'd')
screen.onkeypress(pause, 'p')

screen.ontimer(tick, int(1000/TICK_RATE))

screen.mainloop()
