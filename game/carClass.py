import pygame
import pygameClasses

class Car:
    def __init__(self, max_vel, rotation_vel, car_img,start_xpos,start_ypos):
        self.max_vel = max_vel
        self.rotation_vel = rotation_vel
        self.x_pos = start_xpos
        self.y_pos = start_ypos
        self.Object = pygameClasses.Object(car_img,(self.x_pos,self.y_pos))
        self.car_angle = 0

    def rotate(self, deltaTime ,left=False, right=False):
        if right:
            self.car_angle += self.rotation_vel * deltaTime
        elif left:
            self.car_angle -= self.rotation_vel * deltaTime
        self.Object.Rotate(self.car_angle)