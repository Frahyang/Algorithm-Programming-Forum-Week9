import pygame as p

class Rocket():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = p.image.load("imagesTIY/rocket.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.centerHorizontal = float(self.rect.centerx)
        self.centerVertical = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerHorizontal += self.ai_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerHorizontal -= self.ai_settings.rocket_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centerVertical -= self.ai_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centerVertical += self.ai_settings.rocket_speed_factor

        self.rect.centerx = self.centerHorizontal
        self.rect.centery = self.centerVertical
    def blitme(self):
        self.screen.blit(self.image, self.rect)