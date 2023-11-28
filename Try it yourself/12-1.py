import pygame as p

p.init()

running = True

screen = p.display.set_mode((1280, 720))

p.display.set_caption("Blue Screen")

bg_colour = ("blue")

while running:
    screen.fill(bg_colour)
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    p.display.flip()
    
p.quit()