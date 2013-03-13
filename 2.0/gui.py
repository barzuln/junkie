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
		self.outerPoly = [(100,215),(230,100),(400,150),(560,105),(650,180),(685,270),(710,400),(615,500),(510,545),(355,540),(335,480),(255,490),(185,540),(125,521),(90,420)]
		self.innerPoly = [(150,215),(230,150),(400,200),(540,155),(600,210),(625,275),(650,380),(600,440),(510,500),(380,480),(380,420),(260,430),(185,500),(150,480)]
		self.car = Car(1400,66,0,177,80,350,0, 38, 180,self.innerPoly,self.outerPoly) #mass,power,currentSpeed,maxSpeed,x,y,currentLock, maxLock, orientation
		self.screen = pygame.display.get_surface()
		self.drawStartUp()

	def drawStartUp(self):
		colors = {'black':(0,0,0),'white':(255,255,255),'pink':(255,0,255)}
		self.screen.fill(colors['white'])
		pygame.draw.rect(self.screen, colors['pink'], pygame.Rect(self.car.x, self.car.y, 15, 7))#drawing the car
		pygame.draw.polygon(self.screen, (0,180,0), self.outerPoly,2)
		pygame.draw.polygon(self.screen, (0,180,0), self.innerPoly,2)
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
				self.car.currSpeed += 1
				print self.car.currSpeed
			else:
				pass

	def run(self):
		while True:
			self.input(pygame.event.get())

if  __name__ =='__main__':
	Gui(800,600)