#creating windows
import pygame as py
from pygame.locals import *
def draw_block():
    surface.fill((72,25,8))
    surface.blit(block, (block_x, block_y))
    py.display.flip()
if __name__=="__main__":
    py.init()
    surface=py.display.set_mode((1000,500))
    surface.fill((72,25,8))
    block=py.image.load("C:\\pythonProject\\snake_game\\resources\\snake.jpg").convert()
    block_x=100
    block_y=100
    surface.blit(block,(block_x,block_y))
    py.display.flip()
    running = True
    while running:
        for event in py.event.get():
            if event.type==KEYDOWN:
                if event.key== K_ESCAPE:
                    running=False
                if event.key==K_UP:
                    block_y-=10
                    draw_block()
                if event.key==K_DOWN:
                    block_y+=10
                    draw_block()
                if event.key==K_LEFT:
                    block_x-=10
                    draw_block()
                if event.key==K_RIGHT:
                    block_x+=10
                    draw_block()
            elif event.type==QUIT:
                running=False



