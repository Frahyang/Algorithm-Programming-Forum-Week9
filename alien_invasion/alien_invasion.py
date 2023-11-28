#import sys | no longer needed as module game_functions already has it

import pygame as p

from pygame.sprite import Group

from settings import Settings as S
from game_stats import GameStats as g
from scoreboard import Scoreboard as Sb
from button import Button as b
from ship import Ship as s
import game_functions as gf
def run_game():
    #Initialize pygame, settings, and screen object
    p.init()
    ai_settings = S()
    screen = p.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    p.display.set_caption("Alien Invasion")

    #Make the play button
    play_button = b(ai_settings, screen, "Play")

    #Create an instance to store game statistics
    stats = g(ai_settings)

    #Make a ship, a group of bullets, and a group of aliens
    ship = s(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Create an instance to store the game statistics and create a scoreboard
    sb = Sb(ai_settings, screen, stats)

    #Start the main loop for the game
    while True:
        #Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()