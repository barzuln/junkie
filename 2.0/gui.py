import os, sys
import pygame
from pygame.locals import *

class Gui:
	
	def __init__ (self, width, heigth):
		self.width = width
		self.heigth = heigth
		self.windows = pygame.display.set_mode((width,heigth))
		pygame.display.set_caption("Neuro Junk 2012/13")
		self.screen = pygame.display.get_surface()
		self.drawStartUp()
	
	def drawStartUp(self):
		colors = {'black':(0,0,0),'white':(255,255,255),'pink':(255,0,255)}
		self.screen.fill(colors['black'])
		self.run()
		
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