import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500

player1score = 0
player2score = 0   
game_over = False
player1 = Actor("player1")
player2 = Actor("player1")
player1.pos = 100, 100
player2.pos = 400, 100

target = Actor("target")
target.pos = 250, 100
def draw():
    screen.blit("background", (0, 0))
    player1.draw()
    player2.draw()
    target.draw()
    screen.draw.text("Player 1 Score: " + str(player1score), (10, 10))
    screen.draw.text("Player 2 Score: " + str(player2score), (10, 10))
    if game_over:
        screen.draw.text("Times Up! Your Final Score: " + str(player1score), fontsize = 40, color = "red")
        screen.draw.text("Times Up! Your Final Score: " + str(player2score), fontsize = 40, color = "red")
def place_target():
    target.x = randint(70, WIDTH-70)
    target.y = randint(70, HEIGHT-70)

def time_up():
    global game_over
    game_over = True
def update():
    global score

    if keyboard.left:
        player1.x = player1.x - 2
    if keyboard.right:
        player1.x = player1.x + 2
    if keyboard.up:
        player1.y = player1.y - 2
    if keyboard.down:
        player1.y = player1.y + 2
    if keyboard.a:
        player1.x = player2.x - 2
    if keyboard.d:
        player1.x = player2.x + 2
    if keyboard.w:
        player1.y = player2.y - 2
    if keyboard.s:
        player1.y = player2.y + 2
    player1win = player1.colliderect(target)
    player2win = player2.colliderect(target)

    if player1win:
        player1score += 10
        place_target()
    if player2win:
        player2score += 10
        place_target()

clock.schedule(time_up, 60.0)


pgzrun.go()
