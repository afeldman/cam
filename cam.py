#!/usr/bin/python

import math as m
    
pixelarray = (2048.0,1024.0)
fov = 64.0
 
pixprodeg = map(lambda x: x/fov, pixelarray)
print (pixprodeg)
 
minimalViewDistance = 230.0

def calcf(pixelsize,fov):
    return ((pixelsize/2) / m.tan(m.radians(fov/2)))

f= map(lambda x: calcf(x,fov), pixelarray)
print (f)

pixpromm = map(lambda x: minimalViewDistance /  x, f)
#ppms = "Pixel Pro mm width:\t{:06.5f}\nPixel Pro mm height:\t{:06.5f}".format(pixpromm[0],pixpromm[1])
#print (ppms)
print (pixpromm)

viewsize = map(lambda x,y: minimalViewDistance * x / y, pixelarray, f)
print (viewsize)

'''
def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

if __name__ == "__main__":
   main(sys.argv[1:])'''
