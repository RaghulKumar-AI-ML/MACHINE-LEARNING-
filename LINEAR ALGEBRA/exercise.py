v = [1,2,3,4]
m = [
    [1, 2, 3],
    [4, 5, 6]
]
#identifying the shape of the matrix manually
rows = len(m)
cols = len(m[0]) if len(m) > 0 else 0
print("Shape of the matrix:", (rows, cols))
#using numpy
import numpy as np
matrix = np.array(m)
print("Shape of the matrix using numpy:", matrix.shape)
print("dimension",matrix.ndim)

# add two vectors manually
v1 = [1, 2, 3]
v2 = [4, 5, 6]
for i in range(len(v1)):
    v1[i] += v2[i]
print("Result of vector addition:", v1)
# add two matrices manually
m1 = [
    [1, 2, 3],
    [4, 5, 6]
]
m2 = [
    [7, 8, 9],
    [10, 11, 12]
]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        m1[i][j] += m2[i][j]
print("Result of matrix addition:", m1)
#scaler multiplication of vector using for loop
v3 = [1, 2, 3]
scalar = 2
for i in range(len(v3)):
    v3[i] *= scalar
print("Result of scalar multiplication of vector:", v3)
# implementing using it by numpy
v4 = np.array([1, 2, 3])
scalar = 2
result = v4 * scalar
print("Result of scalar multiplication of vector using numpy:", result)
#implementing dot product of two vectors manually
v5 = [1, 2, 3]#feature vector
v6 = [4, 5, 6]#weight vector
for i in range(len(v5)):
    v5[i] *= v6[i]
dot_product = sum(v5)
print("Dot product of the two vectors:", dot_product)
#implementing dot product using numpy
v7 = np.array([1, 2, 3])
v8 = np.array([4, 5, 6])
dot_product_numpy = np.dot(v7, v8)
print("Dot product of the two vectors using numpy:", dot_product_numpy)
"""
What does each multiplication represent?What does summing represent?
ans --> where we can able to see the feature vector is multiplied with the weight vector and we are able to get the dot product which is the sum of the products of corresponding elements in the two vectors. This operation is fundamental in various applications, including machine learning, where it is used to calculate the output of a linear model based on input features and their corresponding weights.

"""
#matrix multiplication manually
