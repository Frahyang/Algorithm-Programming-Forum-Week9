import pygame as p
p.init()
screen = p.display.set_mode((1280, 720))
running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
        elif event.type == p.KEYDOWN:
            print(event.key)
p.quit()