#!/usr/bin/python

import numpy as np

class image(object):
    def __init__(self, width, height):
        self.height = float(height)
        self.width = float(width)
        self.imagedata = numpy.zeros((self.width, self.height))

    def getSize(self):
        return (self.width, self.height)

    def getPixel(self, u, v):
        return self.imagedata[u,v]
