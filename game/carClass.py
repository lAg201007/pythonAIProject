import pygame
import pygameClasses
import math

class Car:
    def __init__(self, max_vel, aceleration, rotation_vel, car_img,start_xpos,start_ypos):
        self.max_vel = max_vel
        self.rotation_vel = rotation_vel
        self.x_pos = start_xpos
        self.y_pos = start_ypos
        self.Object = pygameClasses.Object(car_img,(self.x_pos,self.y_pos))
        self.car_angle = 0
        self.vel = 0
        self.aceleration = aceleration

    def rotate(self, deltaTime ,left=False, right=False):
        if right:
            self.car_angle += self.rotation_vel * deltaTime
        elif left:
            self.car_angle -= self.rotation_vel * deltaTime
        self.Object.Rotate(self.car_angle)

    def accelerateFoward(self,deltaTime):
        if self.vel < self.max_vel: 
            self.vel += self.aceleration * deltaTime

    def accelerateBackwards(self,deltaTime):
        if self.vel > -self.max_vel:
            self.vel -= self.aceleration * deltaTime

    def desacelerate(self, deltaTime):
        if self.vel > 0:  
            self.vel -= self.aceleration * deltaTime
            if self.vel < 0:  
                self.vel = 0
        elif self.vel < 0: 
            self.vel += self.aceleration * deltaTime
            if self.vel > 0:
                self.vel = 0

    def move(self, deltaTime):
        self.x_pos += self.vel * deltaTime * math.cos(math.radians(self.car_angle))
        self.y_pos += self.vel * deltaTime * math.sin(math.radians(self.car_angle))
        self.Object.UpdateRectPos((self.x_pos, self.y_pos))
