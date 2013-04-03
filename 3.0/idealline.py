# -*- coding: utf-8 -*-

from math import sqrt, sin, cos, pi
from cmath import phase
import pygame
import sys
from pygame.locals import *
from pygame.draw import circle, line, rect, polygon
from pygame import Rect
from car import Car

class TrackSection:
    inner_start = (0,0)
    inner_end = (0,0)
    outer_start = (0,0)
    outer_end = (0,0)

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

def changeField(field, car): 
    """
    Transforms the field around the car.
    
    The coordinate pairs given in field are translated and rotated in a way
    that the car is in (0,0) facing upwards. This transform is applied to the
    field before the ideal line is calculated to simplify further calculations.
    """
    field = [(pt[0]-car.x, pt[1]-car.y) for pt in field]
    
    angle = car.orientation
    
    #x = (x * cos(angle)) - (y * sin(angle))
    #y = (y * cos(angle)) + (x * sin(angle))
    field = [((pt[0] * cos(angle)) - (pt[1] * sin(angle)), (pt[1] * cos(angle)) + (pt[0] * sin(angle))) for pt in field]
    
    return field

def curSection(inner, outer):
    """    
    Returns the section the car is currently in.
    """    
    possible_inner = []
    section = TrackSection()
    
    for i in range(len(inner)-1):
        if inner[i][1] <= 0 and inner[i+1][1] >= 0:
            possible_inner.append((inner[i], inner[i+1]))
    
    if len(possible_inner) == 0:
        return None
    
    section.inner_start = possible_inner[0][0]
    section.inner_end = possible_inner[0][1]
    
    for i in possible_inner:
        if i[0][0] > section.inner_start[0]:
            section.inner_start = i[0]
            section.inner_end = i[1]
    
    possible_outer = []
    
    for i in range(len(outer)-1):
        if outer[i][1] <= 0 and outer[i+1][1] >= 0:
            possible_outer.append((outer[i], outer[i+1]))
    
    if len(possible_outer) == 0:
        return None
    
    section.outer_start = possible_outer[0][0]
    section.outer_end = possible_outer[0][1]
    
    for i in possible_outer:
        if i[0][0] > section.outer_start[0]:
            section.outer_start = i[0]
            section.outer_end = i[1]
    
    return section

def nextSection(field):
    pass

def getIdeal(car, inner, outer):
    inn = changeField(inner)
    out = changeField(outer)
    
    

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
#        elif event.type == KEYDOWN and event.key == 276: #Arrow_LEFT
#            point1[0] -= 20
#            point2[1] -= 20
#        elif event.type == KEYDOWN and event.key == 275: #Arrow_RIGHT
#            point1[0] += 20
#            point2[1] += 20
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            car.x = event.pos[0]
            car.y = event.pos[1]
        elif event.type == MOUSEBUTTONDOWN and event.button == 3:
            carpos = complex(car.x, car.y)
            mpos = complex(event.pos[0], event.pos[1])
            car.orientation = phase(mpos - carpos)
        else:
            print event

radius = 300
point1 = (400,0)
point2 = (0, 400)
car_radius = 30

car = Car(0,0,0,0,0,0,0,0,0,0,0,0,0)
car.x = 420
car.y = 180
car.orientation = pi/2

outer_line = ((100,215),(230,100),(400,150),(560,105),(650,180),(685,270),(710,400),(615,500),(510,545),(355,540),(335,480),(255,490),(185,540),(125,521),(90,420))
inner_line = ((150,215),(230,150),(400,200),(540,155),(600,210),(625,275),(650,380),(600,440),(510,500),(380,480),(380,420),(260,430),(185,500),(150,480))


def runGUI():
    pygame.display.set_mode((800,600))
    pygame.display.set_caption("Neuro Junk 2012/13")
    screen = pygame.display.get_surface()
    
    while True:
        input(pygame.event.get())
        
        screen.fill((0,0,0))
        circle(screen, (255,255,255), (0,0), radius, 1)
        line(screen, (255,255,255), point1, point2, 1)
        
        polygon(screen, (255,255,255), outer_line, 2)
        polygon(screen, (255,255,255), inner_line,2)
        
        if intersectCircle(point1, point2, radius):
            rect(screen, (0,255,0), Rect(600, 200, 100, 100), 0)
        
        inn = changeField(inner_line, car)
        out = changeField(outer_line, car)
        csect = curSection(inn, out)
        
        polygon(screen, (0,0,255), out, 2)
        polygon(screen, (0,0,255), inn, 2)
        
        rect(screen, (255,255,255), Rect(car.x-2, car.y-2, 4, 4), 0)
        
        if csect is not None:
            line(screen, (0,255,0), csect.inner_start, csect.inner_end, 1)
            line(screen, (0,255,0), csect.outer_start, csect.outer_end, 1)
        
        pygame.display.update()
        
    

if __name__ == '__main__':
    runGUI()