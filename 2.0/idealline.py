# -*- coding: utf-8 -*-

from math import sqrt
import pygame
import sys
from pygame.locals import *
from pygame.draw import circle
from pygame.draw import line
from pygame.draw import rect
from pygame import Rect

def intersectCircle(p1, p2, r):
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
    
    if x1 == x2:
        return
    
    k = (y2 - y1)/(x2 - x1)    
    d = y1 - k*x1
    
    a = k**2+1
    b = 2*k*d
    c = d**2 - r**2
    
    root = b**2 - 4*a*c
    
    #if whats under the sqrt is negative there is no intersection
    if root < 0:
        return False
    
    #calculate intersection points
    rx1 = (-b + sqrt(root)) / (2 * a)
    rx2 = (-b - sqrt(root)) / (2 * a)
    
    #calculate y coordinates of intersection points
    ry1 = k*rx1 + d
    ry2 = k*rx2 + d
    
    #check if one of the intersection points is on the given line segement
    betw1 = (x1 <= rx1 <= x2 or x2 <= rx1 <= x1) and (y1 <= ry1 <= y2 or y2 <= ry1 <= y1)
    betw2 = (x1 <= rx2 <= x2 or x2 <= rx2 <= x1) and (y1 <= ry2 <= y2 or y2 <= ry2 <= y1)
    
    return betw1 or betw2

"""
<Event(3-KeyUp {'scancode': 111, 'key': 273, 'mod': 0})> up
<Event(2-KeyDown {'scancode': 116, 'key': 274, 'unicode': u'', 'mod': 0})>
<Event(3-KeyUp {'scancode': 116, 'key': 274, 'mod': 0})> down
<Event(2-KeyDown {'scancode': 113, 'key': 276, 'unicode': u'', 'mod': 0})>
<Event(3-KeyUp {'scancode': 113, 'key': 276, 'mod': 0})> left
<Event(2-KeyDown {'scancode': 114, 'key': 275, 'unicode': u'', 'mod': 0})>
<Event(3-KeyUp {'scancode': 114, 'key': 275, 'mod': 0})> right
"""

def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == KEYDOWN and event.key == 113: #Q
            sys.exit(0)
        elif event.type == KEYDOWN and event.key == 273: #Arrow_UP
            global radius
            radius -= 20
        elif event.type == KEYDOWN and event.key == 274: #Arrow_DOWN
            global radius
            radius += 20
        elif event.type == KEYDOWN and event.key == 276: #Arrow_LEFT
            point1[0] -= 20
            point2[1] -= 20
        elif event.type == KEYDOWN and event.key == 275: #Arrow_RIGHT
            point1[0] += 20
            point2[1] += 20
        else:
            print event

radius = 300
point1 = (400,0)
point2 = (0, 400)


def runGUI():
    window = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Neuro Junk 2012/13")
    screen = pygame.display.get_surface()
    
    while True:
        input(pygame.event.get())
        
        screen.fill((0,0,0))
        circle(screen, (255,255,255), (0,0), radius, 1)
        line(screen, (255,255,255), point1, point2, 1)
        
        if intersectCircle(point1, point2, radius):
            rect(screen, (0,255,0), Rect(600, 200, 100, 100), 0)
        
        pygame.display.update()
        
    

if __name__ == '__main__':
    runGUI()