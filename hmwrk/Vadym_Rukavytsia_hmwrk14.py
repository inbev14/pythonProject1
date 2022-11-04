"""Jumping balls in the window, exit after click on window"""
from random import randint, choice, random
from turtle import Turtle, Screen, exitonclick
from screeninfo import get_monitors
import time


class Window:
    """Make window and have screen wight and height"""
    MONITOR = get_monitors().pop()
    WINDOW_WIDTH = MONITOR.width // 2
    WINDOW_HEIGHT = MONITOR.height // 2
    WINDOW_WIDTH_HALF = WINDOW_WIDTH // 4
    WINDOW_HEIGHT_HALF = WINDOW_HEIGHT // 4
    
    def __init__(self):
        self.window_ = Screen()
        self.window_.title('My first game - Balls !')
        self.window_.setup(width=Window.WINDOW_WIDTH, height=Window.WINDOW_HEIGHT)
        # exitonclick()
        self.window_.listen()
        self.window_.tracer(0)


class Sprite(Turtle):
    """Base object class"""
    def __init__(self):
        super().__init__(shape='circle')
        self.up()
        

class Ball(Sprite):
    """class with ball parameters"""
    size = 20
    
    def __init__(self):
        super().__init__()
        self.shape = 'circle'
        self.color(self.get_rand_color())
        self.goto(self.get_rand_position())
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0

    def move(self):
        self.x = self.xcor()
        self.y = self.ycor()
        self.goto(self.x + self.dx, self.y - self.dy)
        self.dy += 0.01
    
    @staticmethod
    def get_rand_color(color=None):
        if color:
            return color
        return random(), random(), randint(0, 1)
    
    @staticmethod
    def get_rand_position():
        return randint(-Window.WINDOW_WIDTH_HALF, Window.WINDOW_WIDTH_HALF), randint(0, Window.WINDOW_HEIGHT_HALF)


class Game:
    """Making all objects and making it works"""
    def __init__(self, qty_balls: int):
        self.qty_balls = qty_balls
        self.window = Window()
        self.balls = self.make_balls(qty_balls)
    
    def run(self):
        for ball in self.balls:
            ball.dx = 3 * choice((-1, 1))
            ball.dy = 3 * choice((-1, 1))
        
        while True:
            for ball in self.balls:
                ball.move()
                self.check_border(ball)
                self.check_collision(self.balls)
            self.window.window_.update()
            time.sleep(0.000000001)

    @staticmethod
    def make_balls(qty_balls: int):
        return [Ball() for _ in range(qty_balls)]
    
    @staticmethod
    def check_collision(balls: list[Ball]):
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                if balls[i].distance(balls[j]) < 20:  # < Ball.size
                    balls[i].dx, balls[j].dx = balls[j].dx, balls[i].dx
                    balls[i].dy, balls[j].dy = balls[j].dy, balls[i].dy

    @staticmethod
    def check_border(ball):
        x = ball.xcor()
        y = ball.ycor()
        if x > Window.WINDOW_WIDTH_HALF or x < -Window.WINDOW_WIDTH_HALF:
            ball.dx = -ball.dx
        if y < -Window.WINDOW_HEIGHT_HALF:
            ball.dy = -ball.dy
        


if __name__ == '__main__':
    game = Game(25)
    game.run()
    