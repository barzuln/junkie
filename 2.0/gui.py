import os, sys
import pygame
from car import Car
from pygame.locals import *

class Gui:
	
    def __init__ (self, width, heigth):
        self.width = width
        self.heigth = heigth
        self.windows = pygame.display.set_mode((width,heigth))
        pygame.display.set_caption("Neuro Junk 2012/13")
        self.screen = pygame.display.get_surface()
        self.colors = colors = {'black':(0,0,0),'white':(255,255,255),'pink':(255,0,255)}
        self.car = Car(1400,66,0,170,80,80,0,50,0)
        self.drawBackground()
        self.drawCar()

    def drawBackground(self):
        self.screen.fill(self.colors['black'])
        self.update()
        self.run()
    
	def drawCar(self):
		self.car.update(1)
		allsprites = pygame.sprite.RenderPlain(self.car)
		allsprites.draw(self.screen)
		update()
        
    def input(self,events):
        for event in events:
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == 113: #Q
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == 273: #Arrow_UP
                pass
            else:
                print event
                
    def update(self):
        pygame.display.update()

    def run(self):
        while True:
            self.input(pygame.event.get())
		
if  __name__ =='__main__':
	Gui(800,400)