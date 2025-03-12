import pygame

class Texture():
    def __init__(self, image):
        self.Surface = pygame.image.load(image).convert_alpha()
    def Render(self,screenR,pos):
        screenR.blit(self.Surface,pos)

class Object():
    def __init__(self, image, pos):
        self.Surface = pygame.image.load(image).convert_alpha()
        self.Rect = self.Surface.get_rect(topleft=pos)
    def UpdateRectPos(self, pos):
        self.Rect = self.Surface.get_rect(topleft=pos)
    def Render(self, screenR):
        screenR.blit(self.Surface, self.Rect)
    def Scale(self, xy):
        self.Surface = pygame.transform.scale(self.Surface, xy)
    def Rotate(self, angle):
        self.Surface = pygame.transform.rotate(self.Surface, angle)
