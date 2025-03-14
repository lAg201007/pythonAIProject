import carClass
import pygame

class Player(carClass.Car):
    def __init__(self, max_vel, aceleration, desaceleration,breakvel, rotation_vel, car_img, start_xpos, start_ypos):
        super().__init__(max_vel, aceleration, desaceleration,breakvel, rotation_vel, car_img, start_xpos, start_ypos)
        self.key_w = False
        self.key_s = False
        self.key_a = False
        self.key_d = False

    def getInputs(self, event):
        key_map = {
            pygame.K_w: "key_w",
            pygame.K_s: "key_s",
            pygame.K_a: "key_a",
            pygame.K_d: "key_d",
        }

        if event.key in key_map:
            setattr(self, key_map[event.key], True)

    def releaseInputs(self, event):
        key_map = {
            pygame.K_w: "key_w",
            pygame.K_s: "key_s",
            pygame.K_a: "key_a",
            pygame.K_d: "key_d",
        }

        if event.key in key_map:
            setattr(self, key_map[event.key], False)


    def updateInputs(self, deltaTime):
        if self.key_w:
            self.accelerateFoward(deltaTime)
        if self.key_s:
            if self.vel > 0:
                self.desacelerate(deltaTime,self.breakvel)
            else:
                self.accelerateBackwards(deltaTime)
        if self.key_a:
            self.rotate(deltaTime,True)
        if self.key_d:
            self.rotate(deltaTime,False, True)