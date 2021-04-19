import pygame as py
from pygame.locals import *
import random
import time
size_x=53
size_y=43
bg_color=(72,25,8)
class Apple:
    def __init__(self,parent_screen):
        self.image=py.image.load("resources/apple.jpg").convert()
        self.parent_screen=parent_screen
        self.x=size_x*3
        self.y=size_y*3
    def draw(self):
        #self.parent_screen.fill((110, 110, 5))
        self.parent_screen.blit(self.image, (self.x, self.y))
        py.display.flip()
    def move(self):
        self.x=random.randint(0,18)*size_x
        self.y=random.randint(0,9)*size_y

class Snake:
    def __init__(self,parent_screen,length):
        self.length=length
        self.parent_screen=parent_screen
        self.block=py.image.load("resources/snake.jpg").convert()
        self.x=[size_x]*length
        self.y=[size_y]*length
        self.direction='rt'
    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)
    def draw(self):

        for i in range(self.length):
           self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
           py.display.flip()
    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'lt':
            self.x[0] -= size_x
        if self.direction == 'rt':
            self.x[0] += size_x
        if self.direction == 'up':
            self.y[0] -= size_y
        if self.direction == 'dn':
            self.y[0] += size_y
        self.draw()

    def move_left(self):
        self.direction='lt'

    def move_right(self):
        self.direction='rt'

    def move_up(self):
        self.direction='up'

    def move_down(self):
        self.direction='dn'


class Game:
    def __init__(self):
        py.init()
        #mixer module of pygame is for music
        py.mixer.init()
        py.display.set_caption("Developed by Shubham")
        self.play_bg_music()
        self.surface=py.display.set_mode((1000,500))
        self.surface.fill((110,110,5))
        self.snake=Snake(self.surface,1)
        self.snake.draw()
        self.apple=Apple(self.surface)
        self.apple.draw()
    def reset(self):
        self.snake=Snake(self.surface,1)
        self.apple=Apple(self.surface)

    def bg_image(self):
        bg_img=py.image.load("resources/mtblck.jpg")
        self.surface.blit(bg_img,(0,0))


    def play_bg_music(self):
        py.mixer.music.load("resources/bgmusic.mp3")
        py.mixer.music.play()

    def display_score(self):
        font=py.font.SysFont('Calibri Light',30)
        score=font.render(f"Score:{self.snake.length-1}",True,(99,125,11))
        self.surface.blit(score,(800,10))
    def is_collision(self,x1,y1,x2,y2):
         if x1 >= x2 and x1 < x2+size_x:
             if y1 >= y2 and y1 < y2+size_y:
                 return True
         return False

    def play(self):
        self.bg_image()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        py.display.flip()
        #collision with apple
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.snake.increase_length()
            sound= py.mixer.Sound("resources/Ding-sound-effect.mp3")
            py.mixer.Sound.play(sound)
            self.apple.move()
        #collision with itself
        for i in range(3,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                raise "game over"
        #collision with border
        if not(0<=self.snake.x[0] <=1000 and 0<= self.snake.y[0]<=500 ):
            raise "Boundry hit"
    def show_game_over(self):
        self.bg_image()
        sound = py.mixer.Sound("resources/Tada-sound.mp3")
        py.mixer.Sound.play(sound)
        font = py.font.SysFont('Calibri Light', 40)
        disp=font.render(f"Game over! Your Score is : {self.snake.length-1}",True,(102,255,103))
        self.surface.blit(disp,(200,300))
        disp2=font.render(f"To play game press Enter.To quit press Escape!",True,(102,255,103))
        self.surface.blit(disp2, (200, 350))
        py.display.flip()
        py.mixer.music.pause()
    def run(self):
        running=True
        pause=False
        while running:
            for event in py.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_RETURN:
                        pause=False
                        py.mixer.music.unpause()
                        self.snake.length=1
                    if event.key == K_ESCAPE:
                        running = False
                    if not pause:
                      if event.key == K_UP:
                          self.snake.move_up()
                      if event.key == K_DOWN:
                          self.snake.move_down()
                      if event.key == K_LEFT:
                          self.snake.move_left()
                      if event.key == K_RIGHT:
                          self.snake.move_right()
                elif event.type==QUIT:
                    running=False
            try:
                if not pause:
                  self.play()
            except Exception as e:
                self.show_game_over()
                pause=True
                self.reset()
            time.sleep(0.2)




if __name__=="__main__":
    game=Game()
    game.run()
