import pygame as p
import sys
from bulletFive import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == p.K_UP:
        ship.moving_up = True
    elif event.key == p.K_DOWN:
        ship.moving_down = True
    elif event.key == p.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    if event.key == p.K_UP:
        ship.moving_up = False
    elif event.key == p.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets):
    for event in p.event.get():
        if event.type == p.QUIT:
            sys.exit()
        elif event.type == p.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == p.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_colour)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    p.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.left >= 1280:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)