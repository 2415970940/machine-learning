import numpy
vector = numpy.array([1,2,3,4])
matrix = numpy.array([[1,2,3],[4,5,6],[7,8,9]])

print(vector.min())
print(matrix.min())

print(matrix.sum(axis=1))
print(matrix.sum(axis=0))