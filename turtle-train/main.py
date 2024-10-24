import turtle
import random
import TurtleTrain


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
pellet.setposition(random.randint(int((-1 * screen_size[0]/2) + 10), int(screen_size[0]/2 - 10)), random.randint(int((-1 * screen_size[1]/2) + 10), int(screen_size[1]/2 - 10)))

score_text = turtle.Turtle()
score_text.penup()
score_text.goto(screen_size[0]/2 - 30, -1 * (screen_size[1]/2) + 10)
score_text.color(0, 0, 0)
score_text_style = ('Arial', 10, 'bold')
score_text.hideturtle()

def write_score():
    score_text.clear()
    score_text.write(f'Score: {train.score}', font=score_text_style, align='right')


def tick():
    train.move_turtles(5)
    screen.update()
    if not timmy_inbounds(train.get_conductor()):
        game_over()
    if train.intersects(pellet):
        pellet.setposition(random.randint(int((-1 * screen_size[0]/2) + 10), int(screen_size[0]/2 - 10)), random.randint(int((-1 * screen_size[1]/2) + 10), int(screen_size[1]/2 - 10)))
        train.add_turtle()
    for other_turtle in train.turtles[1:]:
        if train.intersects(other_turtle):
            game_over()
    write_score()
    screen.ontimer(tick, int(1000/60))

def face(degrees: int):
    train.turn_train(degrees)

def timmy_inbounds(timmy: turtle.Turtle) -> bool:
    t_x = timmy.xcor()
    t_y = timmy.ycor()
    s_x = float(screen_size[0])/2
    s_y = float(screen_size[1])/2

    return t_x < s_x and t_x > s_x * -1 and t_y < s_y and t_y > s_y * -1

def game_over():
    score_text.clear()
    score_text.goto(0, 0)
    score_text_style = score_text_style = ('Arial', 24, 'bold')
    score_text.write(f'GAME OVER! Score: {train.score}', align='center', font=score_text_style)
    screen.exitonclick()
    exit()

screen.onkeypress(game_over, 'q')
screen.onkeypress(lambda: face(90), 'w')
screen.onkeypress(lambda: face(180), 'a')
screen.onkeypress(lambda: face(270), 's')
screen.onkeypress(lambda: face(0), 'd')

screen.ontimer(tick, int(1000/60))

screen.mainloop()
