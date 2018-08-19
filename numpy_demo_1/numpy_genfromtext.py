import numpy
world = numpy.genfromtxt('abc.txt',delimiter='.',dtype=str)
print(type(world))
print(world)
print(help(numpy.genfromtxt))