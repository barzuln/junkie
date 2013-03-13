import os, sys
import pygame
from pygame.locals import *
from car import Car

class Gui:

	def __init__ (self, width, heigth):
		self.width = width
		self.heigth = heigth
		self.windows = pygame.display.set_mode((width,heigth))
		pygame.display.set_caption("Neuro Junk 2012/13")
		self.car = Car(1400,66,0,177,80,350,0, 38, 180) #mass,power,currentSpeed,maxSpeed,x,y,currentLock, maxLock, orientation
		self.screen = pygame.display.get_surface()
		self.drawStartUp()

	def drawStartUp(self):
		colors = {'black':(0,0,0),'white':(255,255,255),'pink':(255,0,255)}
		self.screen.fill(colors['white'])
		pygame.draw.rect(self.screen, colors['pink'], pygame.Rect(self.car.x, self.car.y, 30, 15))
		pygame.draw.polygon(self.screen, (0,180,0), ((250,100),(300,0),(350,50)))
		self.update()
		self.run()
		
	def update(self):
		pygame.display.update()

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

	def run(self):
		while True:
			self.input(pygame.event.get())

if  __name__ =='__main__':
	Gui(800,400)