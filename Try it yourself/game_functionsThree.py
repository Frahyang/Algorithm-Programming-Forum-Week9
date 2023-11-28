import pygame as p
import sys

def check_keydown_events(event, rocket):
    if event.key == p.K_RIGHT:
        rocket.moving_right = True
    elif event.key == p.K_LEFT:
        rocket.moving_left = True
    elif event.key == p.K_UP:
        rocket.moving_up = True
    elif event.key == p.K_DOWN:
        rocket.moving_down = True

def check_keyup_events(event, rocket):
    if event.key == p.K_RIGHT:
        rocket.moving_right = False
    elif event.key == p.K_LEFT:
        rocket.moving_left = False
    elif event.key == p.K_UP:
        rocket.moving_up = False
    elif event.key == p.K_DOWN:
        rocket.moving_down = False

def check_events(rocket):
    for event in p.event.get():
        if event.type == p.QUIT:
            sys.exit()
        elif event.type == p.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == p.KEYUP:
            check_keyup_events(event, rocket)

def update_screen(ai_settings, screen, rocket):
    screen.fill(ai_settings.bg_colour)
    rocket.blitme()

    p.display.flip()