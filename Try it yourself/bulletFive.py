import pygame as p
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = p.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

        self.x = float(self.rect.x)

        self.colour = ai_settings.bullet_colour
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        p.draw.rect(self.screen, self.colour, self.rect)