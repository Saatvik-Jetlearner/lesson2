import pgzrun
from random import randint
from pgzero.rect import Rect



HEIGHT = 300
WIDTH = 300
def draw(screen):
    red = 255
    green = 0
    blue = randint(100, 255)

    height = HEIGHT
    width = WIDTH - 200 

    for y in range(30):
        rectangle = Rect((0, 0), (height, width))
        rectangle.center = (150, 150)
        screen.draw.rectangle(rectangle, (red, green, blue))

        red -= 10
        green += 10

        height -= 10
        width += 10
    
pgzrun.go()