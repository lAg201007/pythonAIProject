import pygame
import pygameClasses

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    screen.fill((0,0,0))

    # test = pygameClasses.Object("Textures/Image.png", (0,0))
    # test.Render(screen)

    pygame.display.update()

    clock.tick(60) 