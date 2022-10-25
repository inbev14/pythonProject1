from turtle import *
from math import *


class Planet(Turtle):
    def __init__(self, planet_size, planet_color, radius, star, increase_angle, name='star'):
        Turtle.__init__(self, shape='circle')
        self.name = name
        self.speed(0)
        self.shapesize(*planet_size)
        self.x = 0
        self.y = 0
        self.color(planet_color)
        self.up()
        self.angle = 0
        self.increase_angle = increase_angle
        self.radius = radius
        self.star = star

    def move(self):
        self.x = self.radius * cos(self.angle)
        self.y = self.radius * sin(self.angle)
        self.goto(self.star.xcor() + self.x, self.star.ycor() + self.y)
        self.angle += self.increase_angle


SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 950


window = Screen()
window.bgcolor('black')
window.title('Solar system')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')

sun = Turtle(shape='circle')
sun.color('yellow')
sun.shapesize(5, 5)

mercury = Planet((0.8, 0.8), '#8F653F', 70, sun, 0.005)
venus = Planet((1, 1), '#737373', 100, sun, 0.004)
earth = Planet((1, 1), 'blue', 150, sun, 0.003)
moon = Planet((0.4, 0.4), 'grey', 20, earth, 0.02)
mars = Planet((0.8, 0.8), '#F24F2F', 220, sun, 0.002)
jupiter = Planet((2.5, 2.5), '#BF9C8C', 300, sun, 0.001)
saturn = Planet((1.5, 1.5),"grey", 400, sun, 0.0007)
saturn_circle = Planet((2.5, 2.5), 'grey', 0, saturn, 0)



window.listen()

while True:
    
    mercury.move()
    venus.move()
    earth.move()
    moon.move()
    mars.move()
    jupiter.move()
    saturn.move()
    saturn_circle.move()
    window.tracer(3)