import pygame as p
from characterCentered import Centered as c

p.init()
screen = p.display.set_mode((1900, 900))
bg_colour = ("white")
p.display.set_caption("Centered Character")
running = True
character = c(screen)

while running:
    screen.fill(bg_colour)
    character.blitme()
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    p.display.flip()

p.quit()