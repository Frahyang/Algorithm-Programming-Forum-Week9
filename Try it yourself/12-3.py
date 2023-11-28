import pygame as p
from settingsThree import Settings as S
from rocketThree import Rocket as r
import game_functionsThree as gf

p.init()
ai_settings = S()
screen = p.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
p.display.set_caption("Rocket")

rocket = r(ai_settings, screen)

while True:
    gf.check_events(rocket)
    rocket.update()
    gf.update_screen(ai_settings, screen, rocket)