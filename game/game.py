import pygame
import pygameClasses
import time
import carClass
import player

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

game_running = True

dt = 0
FPS = 60
prev_time = time.time()

car = player.Player(400,200,10,400,200,"game/Sprites/red_car.png",screen.get_width() / 2, screen.get_height() / 2)

while game_running:
    clock.tick(FPS)

    now = time.time()
    dt = now - prev_time
    prev_time = now

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        car.input(keys,dt) 
        if event.type == pygame.QUIT:
            game_running = False

    screen.fill((0,0,0))

    car.desacelerate(dt)
    car.move(dt)

    car.Object.Render(screen)

    pygame.display.update()
