import pgzrun
from random import randint
from pgzero.builtins import Rect



HEIGHT = 300
WIDTH = 300
def draw(screen):
    r = 255
    g = 0
    b = randint(100, 255)

    height = HEIGHT
    width = WIDTH - 200 

    for i in range(30):
        rect = Rect((0, 0), (width, height))
        rect.center = 150, 150
        screen.draw.rect(rect, (r, g, b))

        r -= 10
        g += 10

        width -= 10
        height += 10
    
pgzrun.go()