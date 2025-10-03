import pgzrun
from random import randint

TITLE = "Flappy Ball"
WIDTH = 800 
HEIGHT = 600

R = randint(0,255)
G = randint(0,255)
B = randint(0,255)

CLR = R,G,B

GRAVITY = 2000.0

class Ball:
    def _init_(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40
    
    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)

ball1 = Ball(50,100)

def draw():
    screen.clear()
    ball1.draw()
    ball2.draw()

def update(dt):
    uy = ball1.vy
    ball1.vy += GRAVITY * dt
    ball1.y += (uy + ball1.vy) * 0.5 * dt
    #uy = ball2.vy
    #ball2.vy += GRAVITY * dt
    #ball2.y += (uy + ball2.vy) * 0.5 * dt    

    if ball1.y > HEIGHT - ball1.radius:
        ball1.y = HEIGHT - ball1.radius
        ball1.vy = -ball1.vy * 0.9

    #if ball2.y > HEIGHT - ball2.radius:
    #    ball2.y = HEIGHT - ball2.radius
     #   ball2.vy = -ball1.vy * 0.9

    ball1.x += ball1.vx + dt
    if ball1.x > WIDTH - ball1.radius or ball1.x < ball1.radius:
        ball1.vx = -ball1.vx  
    #ball2.x += ball2.vx + dt
    #if ball2.x > WIDTH - ball2.radius or ball2.x < ball2.radius:
    #    ball2.vx = -ball2.vx  

def on_key_down(key):
    """Pressing a key kicks the ball up"""
    if key == keys.SPACE:
        ball1.vy = -500
    #    ball2.vy = -500

pgzrun.go()