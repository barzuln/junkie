import os, sys
import pygame
from pygame.locals import *
from pygame.font import *
from car import Car
import time

class GUI:
	"""works with the computer coordinate system (0/0 top left)"""

	def __init__ (self, width, heigth):
		self.width = width
		self.heigth = heigth
		self.windows = pygame.display.set_mode((width,heigth))
		pygame.display.set_caption("Neuro Junk 2012/13")
		self.outerPoly = [(110,215),(230,100),(400,150),(560,105),(650,180),(685,270),(710,400),(615,500),(510,545),(365,540),(315,480),(255,490),(185,540),(125,521),(90,420)]
		self.innerPoly = [(160,215),(230,150),(400,200),(540,155),(600,210),(625,275),(650,380),(600,440),(510,500),(370,480),(380,420),(260,430),(185,500),(150,480)]
		self.car = Car(1400,0.0,35.0,25.0,0.0,130.0,(120,215),0.0, 38.0, 90.0,(15,15),self.innerPoly, self.outerPoly) 
		#mass,acceleration,maxAcc,maxBreakingForce,currentSpeed,maxSpeed,pos,currentLock, maxLock, orientation, length, width
		self.colors = {'black':(0,0,0),'white':(255,255,255),'pink':(255,0,255)}
		self.screen = pygame.display.get_surface()
		self.drawStartUp()

	def drawStartUp(self):
		self.screen.fill(self.colors['white'])
		self.carRect = pygame.draw.rect(self.screen, self.colors['pink'], pygame.Rect(self.car.convertRealPositionToPc()[0], self.car.convertRealPositionToPc()[1], self.car.convertSizeFromMetersToPixel()[0], self.car.convertSizeFromMetersToPixel()[1]))#drawing the car
		#print "Start:"
		#print "pcx: " + str(self.car.convertRealPositionToPc()[0])
		#print "pcy: " + str(self.car.convertRealPositionToPc()[1])
		pygame.draw.polygon(self.screen, self.colors['black'], self.outerPoly,2)
		pygame.draw.polygon(self.screen, self.colors['black'], self.innerPoly,2)
		self.update()
		self.run()
		
	def update(self):
		self.screen.fill(self.colors['white'])
		pygame.draw.polygon(self.screen, self.colors['black'], self.outerPoly,2)
		pygame.draw.polygon(self.screen, self.colors['black'], self.innerPoly,2)
		self.carRect = pygame.draw.rect(self.screen, self.colors['pink'],pygame.Rect(self.car.convertRealPositionToPc()[0], self.car.convertRealPositionToPc()[1], self.car.convertSizeFromMetersToPixel()[0], self.car.convertSizeFromMetersToPixel()[1]))
		pygame.display.update()

	def drawLines(self,lines):
		for mt in lines:
			pygame.draw.line(self.screen, self.colors['black'], mt[0], mt[1],5)
		pygame.display.update()

	def displayInfo(self):
		pygame.font.init()
		font = pygame.font.SysFont("Ubuntu",15)
		test = font.render("Speed: " + str(self.car.currSpeed),1,(255,0,0))
		self.screen.blit(test, (100,100))
		

	def input(self,events):
		for event in events:
			if event.type == QUIT:
				sys.exit(0)
			elif event.type == KEYDOWN and event.key == 113: #Q
				sys.exit(0)
			elif event.type == KEYDOWN and event.key == 273: #Arrow_UP
				self.car.accelerate(1.0)
				#print self.car.currSpeed
			elif event.type == KEYUP and event.key == 273:
				self.car.accelerate(0.0)
			elif event.type == KEYDOWN and event.key == 274: #Arrow_Down
				self.car.retarding(1.0)
			elif event.type == KEYUP and event.key == 274:
				self.car.retarding(0.0)
			elif event.type == KEYDOWN and event.key == 275: #Arrow_right
				self.car.stiring(-0.25)
			elif event.type == KEYUP and event.key == 275:
				self.car.stiring(0.0)
			elif event.type == KEYDOWN and event.key == 276: #Arrow_left
				self.car.stiring(0.25)
			elif event.type == KEYUP and event.key == 276:
				self.car.stiring(0.0)
			elif event.type == KEYDOWN and event.key == K_SPACE:
				self.car.currSpeed = 0.0
				self.car.acceleration = 0.0
			else:
				pass

	def run(self):
		lines = []
		while True:
			self.input(pygame.event.get())
			mt = self.car.nextPos(0.01)
			self.update()
			#print "mt: " + str(mt)
			#lines.append(mt)
			#self.drawLines(lines)
			time.sleep(0.01)

if  __name__ =='__main__':
	GUI(800,600)