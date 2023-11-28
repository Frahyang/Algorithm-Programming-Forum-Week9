import pygame as p
from pygame.sprite import Group
from settingsFive import Settings as S
from shipFive import Ship as s
import game_functionsFive as gf

p.init()
ai_settings = S()

screen = p.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
p.display.set_caption("Sideways Shooter")

ship = s(ai_settings, screen)
bullets = Group()
while True:
    gf.check_events(ai_settings, screen, ship, bullets)
    ship.update()
    gf.update_bullets(bullets)
    gf.update_screen(ai_settings, screen, ship, bullets)