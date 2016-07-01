#!/usr/bin/python
 
pixelarray = (2048.0,1024.0)
fov = 64.0
 
pixprodeg = pixelarray[0]/fov
 
print (pixprodeg)
 
import math as m
 
minimalViewDistance = 230.0

f = (pixelarray/2) / tan(deg2rad(fov/2));

pixpromm = minimalViewDistance /  f;

viewwidth = minimalViewDistance * pixelarray /  f;

#Pixpromm = viewwidth / pixelarray
#= minimalViewDistance /  f
#= minimalViewDistance  * tan(deg2rad(fov/2)) / (pixelarray/2)
