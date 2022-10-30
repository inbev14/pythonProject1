"""Jumping balls in the window, exit after click on window"""
from random import randint, choice
from turtle import Turtle, Screen, exitonclick
from screeninfo import get_monitors


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
        exitonclick()
        self.window_.listen()
        self.window_.tracer(0)


class Sprite(Turtle):
    """Base object class"""
    def __init__(self, shape):
        super().__init__(shape)
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
        self.dy += 0.1
    
    @staticmethod
    def get_rand_color(color=None):
        if color:
            return color
        return randint(0, 255), randint(0, 255), randint(0, 255)
    
    @staticmethod
    def get_rand_position():
        return randint(-Window.WINDOW_WIDTH, Window.WINDOW_WIDTH), randint(0, Window.WINDOW_HEIGHT_HALF)


class Game:
    """Making all objects and making it works"""
    
    def __init__(self, qty_balls: int):
        self.qty_balls = qty_balls
        self.window = Window()
        self.balls = self.make_balls(qty_balls)
    
    def run(self):
        for ball in self.balls:
            ball.dx = 2 * choice((-1, 1))
            ball.dy = 2
        
        while True:
            for ball in self.balls:
                ball.move()
                self.check_border(ball)
            self.window.window_.update()
            self.check_collision(self.balls)

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

        if y < -Window.WINDOW_HEIGHT:
            ball.dy = -ball.dy
        if x > Window.WINDOW_WIDTH_HALF or x < -Window.WINDOW_WIDTH_HALF:
            ball.dx = -ball.dx


if __name__ == '__main__':
    game = Game(10)
    game.run()
    