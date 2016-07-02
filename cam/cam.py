#!/usr/bin/python

import math as m
import numpy as np

class image(object):
    def __init__(self, width, height):
        self.height = float(height)
        self.width = float(width)
        self.imagedata = numpy.zeros((self.width, self.height))

    def getSize(self):
        return (self.width, self.height)
        
class cam(object):
    def __init__(self, image, fieldofview = 50, minimalViewDistance=0.0):
        self.image = image
        self.fov = float(fieldofview)
        self.mvd = float(minimalViewDistance)
        
        self.f = self.getFocalLength()
        self.ppd = self.getPixelProDeg()
        
    def getFocalLength(self): 
        return map(lambda x: ((x/2) / m.tan(m.radians(self.fov/2))), self.image.getSize())

    def getPixelProDeg(self):
        return map(lambda x: x/fov, self.image.getSize())

    def PixelProMM(self):
        return map(lambda x: self.mvd /  x, self.f)

    def getViewSize(self):
        return map(lambda x,y: self.mvd * x / y, self.image.getSize(), self.f)
