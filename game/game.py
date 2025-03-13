import pygame
import pygameClasses
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

game_running = True

dt = 0
FPS = 60
prev_time = time.time()

while game_running:
    clock.tick(FPS)

    now = time.time()
    dt = now - prev_time
    prev_time = now

    # exemplo usando dt: object_xpos = xvelocity * dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    screen.fill((0,0,0))

    # test = pygameClasses.Object("Textures/Image.png", (0,0))
    # test.Render(screen)

    pygame.display.update()
