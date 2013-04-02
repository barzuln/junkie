import os, sys
import pygame
from pygame.locals import *
import math
class Car:
	"""works with the carthesian coordinate system (0/0 bottom left)"""

	def __init__ (self,mass,acceleration,maxAcc,maxBrakingForce,currentSpeed,maxSpeed,pos,currentLock, maxLock, orientation, size, innerPoly, outerPoly):
		self.mass = mass #kg
		self.acceleration = acceleration #meters/seconds
		self.maxAcc = maxAcc
		self.maxBrakingForce = maxBrakingForce
		self.currSpeed = currentSpeed #meters/seconds
		self.maxSpeed = maxSpeed #meters/seconds
		self.pos = self.convertPcPositionToReal(pos) #meter
		self.currLock = currentLock
		self.maxLock = maxLock
		self.orientation = orientation
		self.size = self.convertSizeFromPixelToMeters(size) #in meter 
		self.innerPoly = self.convertPixelPolygonToMeters(innerPoly) #course Points inside
		self.outerPoly = self.convertPixelPolygonToMeters(outerPoly) #course Points outside
		self.windowHeight = 600 

	def convertPcPositionToReal(self, pos):
		realx = pos[0]*3.5
		realy = (600-pos[1])*3.5
		return (realx,realy)

	def convertRealPositionToPc(self):
		pcx = self.pos[0]/3.5
		pcy = (600-(self.pos[1]/3.5))
		return (pcx, pcy)

	def convertSizeFromPixelToMeters(self, size):
		return (size[0]*3.5,size[1]*3.5)

	def convertSizeFromMetersToPixel(self):
		return (self.size[0]/3.5,self.size[1]/3.5)

	def convertPixelPolygonToMeters(self, poly):
		converted = []
		for entry in poly:
			realx = entry[0]*3.5
			realy = (600-entry[1])*3.5
			converted.append((realx,realy))
		#print "Converted Polygon: "
		#print converted
		return converted

	def convertMeterPolygonToPixel(self, poly):
		converted = []
		for entry in poly:
			pcx = entry[0]/3.5
			pcy = 600-(entry[1]/3.5)
			converted.append((pcx,pcy))
		return converted

	def updatePosition(self, newpos, newangle):
		self.pos = newpos
		self.orientation = newangle
		#print "Updating Position to: " + str(newpos)

	def accelerate(self, accperc): #accperc [0,1]
		self.acceleration = (accperc * self.maxAcc)

	def retarding(self, breakperc): #breakperc [0,1] (bremsen look at dict.cc)
		self.acceleration -= (breakperc * self.maxBrakingForce)

	def stiring(self, newlock): #newlock [-1,1]
		self.currLock = (newlock * self.maxLock)

	def nextPos(self, time):
		phi = self.currLock
		#print "phi: " + str(phi)
		v2 = self.currSpeed + self.acceleration * time
		va = ( v2 + self.currSpeed) / 2
		s = va * time
		eps = phi/2
		#print "eps: " + str(eps)
		x = (math.sin(math.radians(eps)) * ((s/2)/(math.sin(math.radians((180 - eps))))))
		if (self.orientation + eps) == 90.0000 or (self.orientation + eps) == 270.00000:
			self.orientation += 0.01
		if x == 0:
			b = s * math.sin(math.radians(self.orientation))
			a = s * math.sin(math.radians(90 - (self.orientation)))
		else:
			b = 2 * x * math.sin(math.radians(self.orientation + eps))
			a = 2 * x * math.sin(math.radians(90 - (self.orientation + eps)))

		q = self.orientation + eps 
		
		x2 =  self.pos[0] + a
		y2 = self.pos[1] + b
		self.currSpeed = v2	
		if not self.collision(self.innerPoly, (self.pos[0], self.pos[1]), (x2, y2)) and not self.collision(self.outerPoly, (self.pos[0], self.pos[1]), (x2, y2)):	
			self.updatePosition((x2, y2), (self.orientation + eps))	
		else:
			print "WAND!"
			#print "currpos: " + str(self.pos)
			#print "nextpos: " + str(x2) + "/" + str(y2)
			self.currSpeed = 0.0
			self.acceleration = 0.0
		return self.drawLine((self.pos[0], self.pos[1]), (x2, y2))
		
			
	def collision(self, polygon, carpos1, carpos2):
		for i in range(0, len(polygon)-1, 1):
			p1 = polygon[i]
			p2 = 0.0
			k = 0.0
			k2 = 0.0
			if i < (len(polygon)-1):
				p2 = polygon[i + 1]
				#print "setting p2 to " + str(p2)
			else:
				p2 = polygon[0]
			if p2[0] == p1[0] and p2[1] == p1[1]:
				return False
			if p2[0] != p1[0]:
				k = (p2[1] - p1[1]) / (p2[0] - p1[0])
			else:
				pass
				#print "hier bin ich in diesem fall"
			d = p1[1] - k * p1[0]

			if carpos2[0] == carpos1[0] and carpos2[1] == carpos1[1]:
				return False
			if carpos2[0] != carpos1[0]:
				k2 = (carpos2[1] - carpos1[1])/(carpos2[0] - carpos1[0])
			else:
				pass
				#print "oarsch"
			d2 = carpos1[1] - k2 * carpos1[0]
			
			if k != k2:
				xs = (d - d2) / (k2 - k)
				##print xs
							
			if min(carpos1[0], carpos2[0]) < xs < max(carpos1[0], carpos2[0]):
				#print "Collsion detected"
				return True
		return False

	def drawLine(self, carpos1, carpos2):
		rc1 = ((carpos1[0]/3.5),(600-(carpos1[1]/3.5)))
		rc2 = ((carpos2[0]/3.5),(600-(carpos2[1]/3.5)))
		return (rc1,rc2)


			