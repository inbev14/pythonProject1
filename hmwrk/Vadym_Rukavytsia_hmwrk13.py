from turtle import *
from math import *
import random
import time


class Planet(Turtle):
    def __init__(self, planet_size, planet_color, radius, star, increase_angle):
        Turtle.__init__(self, shape='circle')
        self.speed(0)
        self.shapesize(*planet_size)
        self.x = 0
        self.y = 0
        self.color(planet_color)
        self.up()
        self.angle = random.randint(10, 150)
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
window.tracer(0)


sun = Turtle(shape='circle')
sun.color('yellow')
sun.shapesize(5, 5)

mercury = Planet((0.8, 0.8), '#8F653F', 70, sun, 0.005)
venus = Planet((1, 1), '#737373', 100, sun, 0.004)
earth = Planet((1, 1), 'blue', 150, sun, 0.003)
moon = Planet((0.4, 0.4), 'grey', 20, earth, 0.02)
mars = Planet((0.8, 0.8), '#F24F2F', 220, sun, 0.002)
phobos = Planet((0.4, 0.4), 'grey', 30, mars, 0.03)
deimos = Planet((0.2, 0.2), 'white', 40, mars, 0.05)
jupiter = Planet((2.5, 2.5), '#BF9C8C', 300, sun, 0.001)
saturn = Planet((1.5, 1.5), 'orange', 300, sun, 0.002)

planets = [mercury, venus, earth, moon, mars, phobos, deimos, jupiter, saturn]
saturn_asteroids = []
asteroids = []
angle = 0.002

for _ in range(200):
    asteroid = Planet((0.2, 0.2), 'white', 40, saturn, 0.01)
    saturn_asteroids.append(asteroid)
    asteroid.increase_angle += angle
    angle += 0.001
    
for _ in range(500):
    asteroid = Planet((0.1, 0.1), 'white', random.randint(400, 550), sun, 0.01)
    asteroids.append(asteroid)
    asteroid.increase_angle += angle
    angle += 0.0031
    
window.listen()


while True:
    window.update()
    for planet in planets:
        planet.move()
    for sat_aster in saturn_asteroids:
        sat_aster.move()
    for aster in asteroids:
        aster.move()
    time.sleep(0.000000002)
