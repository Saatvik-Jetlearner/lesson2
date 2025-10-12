import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 800

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

img = pygame.image.load("bg.jpg")
image = pygame.transform.scale(img, (WIDTH, HEIGHT))


while(True):
    font = pygame.font.SysFont("Times New Roman", 72)
    text = font.render("Happy", True, (0,0,0))
    text2 = font.render("Birthday", True, (0,0,0))
    display_surface.fill((255, 255, 255))
    display_surface.blit(image, (0, 0))
    display_surface.blit(text, (210,180))
    display_surface.blit(text2, (180,264))
    pygame.display.update()
    time.sleep(2)

    img1 = pygame.image.load("image2.jpg")
    image = pygame.transform.scale(img1, (WIDTH, HEIGHT))
    text3 = font.render("Wish You a", True, (0,0,0))
    text4 = font.render("Great Birthday!", True, (0, 0, 0))
    display_surface.fill((255, 255, 255))
    display_surface.blit(image, (0, 0))
    display_surface.blit(text3, (120,150))
    display_surface.blit(text4, (120,210))
    pygame.display.update()
    time.sleep(2)
    display_surface.fill((255, 255, 255))
    pygame.display.update()
    time.sleep(2)
