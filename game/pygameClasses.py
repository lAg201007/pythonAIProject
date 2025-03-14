import pygame

class Texture():
    def __init__(self, image):
        self.Surface = pygame.image.load(image).convert_alpha()
    def Render(self,screenR,pos):
        screenR.blit(self.Surface,pos)

class Object():
    def __init__(self, image, pos):
        self.Surface = pygame.image.load(image).convert_alpha()
        self.original_surface = self.Surface 
        self.Rect = self.Surface.get_rect(center=pos)
        self.Position = pos
        self.angle = 0  

    def UpdateRectPos(self, pos):
        self.Rect = self.Surface.get_rect(center=pos)
        self.Position = pos

    def Render(self, screenR):
        self.UpdateRectPos(self.Position)
        screenR.blit(self.Surface, self.Rect)

    def Scale(self, xy):
        self.Surface = pygame.transform.scale(self.original_surface, xy)

    def Rotate(self, angle):
        if angle != self.angle:  
            self.Surface = pygame.transform.rotate(self.original_surface, angle)
            self.angle = angle 

            # Recalcula o retângulo para a nova posição da imagem rotacionada
            self.Rect = self.Surface.get_rect(center=self.Position)
