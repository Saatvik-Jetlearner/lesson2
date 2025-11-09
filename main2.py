import pygame
pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Square, Circle, Rectangle, Line Demo")
pygame.draw.rect(screen, (0, 0, 255), (300, 300, 25, 25))
pygame.display.update()
