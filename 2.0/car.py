import os, sys
import pygame
from pygame.locals import *

class Car:
	#lock...Lenkeinschlag
	def __init__ (self,mass,acceleration,currentSpeed,maxSpeed,pos,currentLock, maxLock, orientation, size):
		self.mass = mass #kg
		self.acceleration = acceleration #meters/seconds
		self.currSpeed = currentSpeed #meters/seconds
		self.maxSpeed = maxSpeed #meters/seconds
		self.position = pos
		self.currLock = currentLock
		self.maxLock = maxLock
		self.orientation = orientation
        self.size = size #in meter 
        
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
		#car.updatePosition(x2, y2, (Car.orientation + eps))
	elif 90 < q <= 180:
		#2.Quadrant
		x2 =  car.x - a
		y2 = car.y + b
		#car.updatePosition(x2, y2, (Car.orientation + eps))
	elif 180 < q <= 270:
		#3.Quadrant
		x2 =  car.x - a
		y2 = car.y - b
		#car.updatePosition(x2, y2, (Car.orientation + eps))
	else: 
		#4.Quadrant
		x2 =  car.x + a
		y2 = car.y - b
		
	if collision(self.innerPoly, (self.x, self.y), (x2, y2)) && collision(self.outerPoly, (self.x, self.y), (x2, y2)):	
		car.updatePosition(x2, y2, (Car.orientation + eps))	
	else:
		print "HURNS WAND!"
	
    def collision(polygon, carpos1, carpos2):
        
        for i in range(0, len(polygon)-1, 1):
            p1 = polygon[i]
            p2 = 0
            if i < (len(polygon)-1)
                p2 = polygon[i + 1]
            else:
                p2 = polygon[0]
            
            k = (p2[1] - p1[1]) / (p2[0] - p1[0])
            d = p1[1] - k * p1[0]
            
            k2 = (carpos2[1] - carps1[1])/(carpos2[0] - carpos1[0])
            d2 = carpos1[1] - k * carpos1[0]
            
            xs = (d2 - d) / (k - k2)
            
            if min(carpos1[0], carpos2[0]) < xs < max(carpos1[0], carpos2[0]):
                return True
            
        return False
        
    def convertSizeToPixel(self, size):
        return (size[0]*3,5,size[1]*3,75)
        