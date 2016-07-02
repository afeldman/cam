#!/usr/bin/python

import math as m
from cam import image
        
class cam(object):
    def __init__(self, image, fieldofview = 50, minimalViewDistance=0.0):
        self.image = image
        self.fov = float(fieldofview)
        self.mvd = float(minimalViewDistance)
        
        self.f = map(lambda x: ((x/2) / m.tan(m.radians(self.fov/2))), self.image.getSize())
        self.ppd = map(lambda x: x/fov, self.image.getSize())
        
    def getFocalLength(self): 
        return self.f

    def getPixelProDeg(self):
        return self.ppd

    def PixelProMM(self):
        return map(lambda x: self.mvd /  x, self.f)

    def getViewSize(self):
        return map(lambda x,y: self.mvd * x / y, self.image.getSize(), self.f)
