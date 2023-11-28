import pygame as p

class Centered():
    def __init__(self, screen):
        self.screen = screen

        self.image = p.image.load("imagesTIY/Zhongli.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)