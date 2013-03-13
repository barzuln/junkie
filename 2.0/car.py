import os, sys
import pygame
from pygame.locals import *

class Car:
	#lock...Lenkeinschlag
	def __init__ (self,mass,power,currentSpeed,maxSpeed,x,y,currentLock, maxLock, orientation):
		self.mass = mass
		self.power = power
		self.currSpeed = currentSpeed
		self.maxSpeed = maxSpeed
		self.x = x
		self.y = y
		self.currLock = currentLock
		self.maxLock = maxLock
		self.orientation = orientation

	def updatePosition(self,newX,newY,newAngle):
		self.x = newX
		self.y = newY
		self.orientation = newAngle

	def nextPos(time):
		
		phi = Car.currLock

		v2 = Car.currSpeed + getAcc() * time
		va = ( v2 + Car.currSpeed) / 2
		s = va * time
		r = ((s/2)/(math.sin(math.radians( phi/2))))*(math.sin(math.radians((180-phi)/2)))
		eps= phi/2

		x=math.sin(math.radians(eps)) * ((s/2)/(math.sin(math.radians(180 - phi))))

		if x == 0:
			b = s * math.sin(math.radians(Car.orientation + eps))
			a = s * math.sin(math.radians(90 - (Car.orientation + eps)))
		else:
			b = 2 * x * math.sin(math.radians(Car.orientation + eps))
			a = 2 * x * math.sin(math.radians(90 - (Car.orientation + eps)))


		q = Car.orientation + eps 
		if 0 < q <= 90:
			#1.Quadrant
			x2 = car.x + a
			y2 = car.y + b
			car.updatePosition(x2, y2, (Car.orientation + eps))
		elif 90 < q <= 180:
			#2.Quadrant
			x2 =  car.x - a
			y2 = car.y + b
			car.updatePosition(x2, y2, (Car.orientation + eps))
		elif 180 < q <= 270:
			#3.Quadrant
			x2 =  car.x - a
			y2 = car.y - b
			car.updatePosition(x2, y2, (Car.orientation + eps))
		else: 
			#4.Quadrant
			x2 =  car.x + a
			y2 = car.y - b
			car.updatePosition(x2, y2, (Car.orientation + eps))
