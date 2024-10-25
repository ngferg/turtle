from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,  screen_size: tuple):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(screen_size[0]/2 - 30, -1 * (screen_size[1]/2) + 10)
        self.color(0, 0, 0)
        self.score_text_style = ('Arial', 10, 'bold')
    
    def write_score(self, score: int):
        self.clear()
        self.write(f'Score: {score}', font=self.score_text_style, align='right')

    def write_game_over(self, score: int):
        self.clear()
        self.goto(0, 0)
        self.score_text_style = ('Arial', 24, 'bold')
        self.write(f'GAME OVER! Score: {score}', align='center', font=self.score_text_style)
    
    def write_paused(self):
        self.clear()
        self.write('Paused', font=self.score_text_style, align='right')
