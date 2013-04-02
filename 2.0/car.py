import os, sys
import pygame
from pygame.locals import *
import math

class Car:
	#lock...Lenkeinschlag
	def __init__ (self,mass,acceleration,currentSpeed,maxSpeed,pos,currentLock, maxLock, orientation, size, innerPoly, outerPoly):
		self.mass = mass #kg
		self.acceleration = acceleration #meters/seconds
		self.currSpeed = currentSpeed #meters/seconds
		self.maxSpeed = maxSpeed #meters/seconds
		self.position = pos #meter
		self.currLock = currentLock
		self.maxLock = maxLock
		self.orientation = orientation
		self.size = size #in meter 
		self.innerPoly = innerPoly #course Points inside
		self.outerPoly = outerPoly #course Points outside        

	def updatePosition(self,newX,newY,newAngle):
		self.position = (newX,newY)
		self.orientation = newAngle
		
	def convertSizeToPixel(self): #from meters to pixel
		return (self.size[0]*3.5,self.size[1]*3.5)

	def convertPositionToPixel(self): #from meters to pixel
		return (self.position[0]*3.5,(self.position[1]*3.5))

	def convertPolygonToMeters(self, pixel):
		return (pixel[0]/3.5,600-pixel[1]/3.5)

	def nextPos(self, time):
		phi = self.currLock
		print "phi " + str(phi)
		v2 = self.currSpeed + self.acceleration * time
		va = ( v2 + self.currSpeed) / 2
		s = va * time
		#r = ((s/2)/(math.sin(math.radians(phi/2))))*(math.sin(math.radians((180-phi)/2)))
		eps = phi/2
		print "eps: " + str(eps)
		x = (math.sin(math.radians(eps)) * ((s/2)/(math.sin(math.radians((180 - eps))))))
		print "x: " + str(x)

		if x == 0:
			b = s * math.sin(math.radians(self.orientation))
			a = s * math.sin(math.radians(90 - (self.orientation)))
		else:
			b = 2 * x * math.sin(math.radians(self.orientation + eps))
			a = 2 * x * math.sin(math.radians(90 - (self.orientation + eps)))

		q = self.orientation + eps 
		print "q: " + str(q)
		
		if 0 < q <= 90: #1.Quadrant
			x2 = self.position[0] + a
			y2 = self.position[1] + b
		elif 90 < q <= 180:
			#2.Quadrant
			x2 =  self.position[0] - a
			y2 = self.position[1] + b
		elif 180 < q <= 270: #3.Quadrant
			x2 =  self.position[0] - a
			y2 = self.position[1] - b
		else: #4.Quadrant
			x2 =  self.position[0] + a
			y2 = self.position[1] - b
			
		if not self.collision(self.innerPoly, (self.position[0], self.position[1]), (x2, y2)) and not self.collision(self.outerPoly, (self.position[0], self.position[1]), (x2, y2)):	
			self.updatePosition(x2, y2, (self.orientation + eps))	
		else:
			print "WAND!"
			print "currpos: " + str(self.position)
			print "nextpos: " + str(x2) + "/" + str(y2)
			sys.exit(0)
		self.currSpeed = v2
			
	def collision(self, polygon, carpos1, carpos2):
		for i in range(0, len(polygon)-1, 1):
			p1 = self.convertPolygonToMeters(polygon[i])
			p2 = 0.0
			k = 0.0
			k2 = 0.0
			if i < (len(polygon)-1):
				p2 = self.convertPolygonToMeters(polygon[i + 1])
			else:
				p2 = self.convertPolygonToMeters(polygon[0])
			if p2[0] == p1[0] and p2[1] == p1[1]:
				return False
			if p2[0] == p1[0]:
				k = 0.0
			else:
				k = (p2[1] - p1[1]) / (p2[0] - p1[0])
			d = p1[1] - k * p1[0]
			if carpos2[0] == carpos1[0] and carpos2[1] - carpos1[1]:
				return False
			if carpos2[0] == carpos1[0]:
				k2 = 0.0
			else:
				k2 = (carpos2[1] - carpos1[1])/(carpos2[0] - carpos1[0])
			d2 = carpos1[1] - k * carpos1[0]
			
			if k != k2:
				xs = (d2 - d) / (k - k2)
							
			if min(carpos1[0], carpos2[0]) < xs < max(carpos1[0], carpos2[0]):
				return True
		return False 
