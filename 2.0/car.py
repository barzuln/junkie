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
        self.image, self.rect = self.load_image('car.png')
        self.punching = 0

    def updatePosition(self,newX,newY,newAngle):
        self.x = newX
        self.y = newY
        self.orientation = newAngle

    def nextPos(time):
        pass

    def load_image(name, colorkey=None):
        fullname = os.path.join('images', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print 'Cannot load image:', fullname
            raise SystemExit, message
        image = image.convert()
        """ if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)"""
        return image, image.get_rect()