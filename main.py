import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))
pygame.display.update()
subway_surfer = pygame.image.load("subwaysurfers.png")
roblox = pygame.image.load("roblox.png")
minecraft = pygame.image.load("minecraft.png")
clashroyale = pygame.image.load("clashroyale.png")
screen.blit(subway_surfer, (150, 100))
screen.blit(roblox, (150, 200))
screen.blit(minecraft, (150, 300))
screen.blit(clashroyale, (150, 400))
font = pygame.font.SysFont("Times New Roman", 36)
text = font.render("Roblox", True, (0, 0, 0))
text1 = font.render("Clash Royale", True, (0, 0, 0))
text2 = font.render("Subway Surfers", True, (0, 0, 0))
text3 = font.render("Minecraft", True, (0, 0, 0))
screen.blit(text, (350, 100))
screen.blit(text1, (350, 200))
screen.blit(text2, (350, 300))
screen.blit(text3, (350, 400))
pygame.display.update()

while 1:

    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (100, 100, 0), (pos), 20, 0)
            pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
            pos1 = pygame.mouse.get_pos()
            pygame.draw.line(screen, (100, 100, 0), (pos), (pos1), 5)
            pygame.draw.circle(screen, (0, 0, 255), (pos1), 20, 0)
            pygame.display.update()

