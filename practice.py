import numpy as np
arra = np.array([1,2,3,4,5])
print(arra)
print(sep="/")

mat = np.array([[1,2],[3,4]])
print(mat)
print(sep="/")

#create a 3d array (matrix)
mat3d = np.array([[1,2],[3,4],[5,6]])
print(mat3d)
print(sep="/")

#print a list
list = np.array([1,2,3,4,5])
print(list)
print(sep="/")

zeros = np.zeros((3,3))
print(zeros)
print(sep="/")

identity = np.identity(3)
print(identity)
print(sep="/")
print(arra*2)
print(sep="/")

#matrix multiplication
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
mt = np.dot(a,b)
print(mt)
print(sep="/")

#array indexing
arrays = np.array([1,2,3,4,5,6,7,8])
print(arrays[2])
print(sep="/")

