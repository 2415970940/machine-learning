import numpy
matrix = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix[1,1])
print(matrix[1,])
print(matrix[:,1])

vector = numpy.array([1,2,3,4])
print(vector == 1)
index = (matrix == 4)
print(index)
print(matrix[index])