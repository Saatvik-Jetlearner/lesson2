import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0  
game_over = False

bee = Actor("bee")
bee.pos = 100,100

flower = Actor("flower")
flower.pos = 200,200

def draw():
    screen.blit("background", (0, 0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: " + str(score), (10, 10))
    if game_over:
        screen.draw.text("Times Up! Your Final Score: " + str(score), fontsize = 40, color = "red")

def place_flower():
    flower.x = randint(70, WIDTH-70)
    flower.y = randint(70, HEIGHT-70)

def time_up():
    global game_over
    game_over = True
def update():
    global score

    if keyboard.left:
        bee.x = bee.x - 2
    if keyboard.right:
        bee.x = bee.x + 2
    if keyboard.up:
        bee.y = bee.y - 2
    if keyboard.down:
        bee.y = bee.y + 2

    flower_collected = bee.colliderect(flower)  

    if flower_collected:
        score = score + 10
        place_flower()

clock.schedule(time_up, 60.0)


pgzrun.go()