import carClass
import pygame

class Player(carClass.Car):
    def __init__(self, max_vel, aceleration, desaceleration,breakvel, rotation_vel, car_img, start_xpos, start_ypos):
        super().__init__(max_vel, aceleration, desaceleration,breakvel, rotation_vel, car_img, start_xpos, start_ypos)

    def input(self,keys,deltaTime):
        if keys[pygame.K_w]:
            self.accelerateFoward(deltaTime)
        if keys[pygame.K_s]:
            if self.vel > 0:
                self.desacelerate(deltaTime,self.breakvel)
            else:
                self.accelerateBackwards(deltaTime)
        if keys[pygame.K_a]:
            self.rotate(deltaTime,True)
        if keys[pygame.K_d]:
            self.rotate(deltaTime,False, True)