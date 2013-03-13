import os, sys
import pygame
from pygame.locals import *

class Car(pygame.sprite.Sprite):
	#lock...Lenkeinschlag
	def __init__ (self,mass,power,currentSpeed,maxSpeed,x,y,currentLock, maxLock, orientation):
		pygame.sprite.Sprite.__init__(self)
		self.mass = mass
		self.power = power
		self.currSpeed = currentSpeed
		self.maxSpeed = maxSpeed
		self.x = x
		self.y = y
		self.currLock = currentLock
		self.maxLock = maxLock
		self.orientation = orientation
		self.image = pygame.image.load("car.png")
		self.image = self.image.convert_alpha()
		self.rect = self.image.get_rect()
		
	def update(self,seconds):
		self.rect.center = pygame.mouse.get_pos()

	def updatePosition(self,newX,newY,newAngle):
		self.x = newX
		self.y = newY
		self.orientation = newAngle

	def nextPos(time):
		pass
