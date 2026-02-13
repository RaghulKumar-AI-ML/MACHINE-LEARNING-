"task1"
"""🔹 Your Task

Create an array:

arr = np.array([10, 20, 30, 40, 50])


Compute:

mean

standard deviation

Normalize the array using vectorization (NO LOOPS).

Print:

Original array

Normalized array"""
"task1 solution"
import numpy as np
arr=np.arange(10)
print(arr)
meann = np.mean(arr)
print(meann)
stand=np.std(arr)
print(stand)
"vectorization can be done by  dot product also am i correct? "
normaliszed_array=(arr-meann)/stand
print(normaliszed_array)

"task2 "
"""
🧪 TASK 2 — Max, Min, Argmax

Given:

arr = np.array([5, 12, 3, 19, 7])


Find:

Maximum value

Minimum value

Index of maximum value

Use:

np.max()

np.min()

np.argmax()
"""
"task2 solution"
arr2 = np.array([5, 12, 3, 19, 7])
print(np.max(arr2))
print(np.min(arr2))
print(np.argmax(arr2))
print(np.argmin(arr2))

"""🧪 TASK 3 — Row-wise & Column-wise Mean

Given:

mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])


Compute:

Mean of each row

Mean of each column

Hint:

np.mean(mat, axis=?)


Remember:

axis=0 → column-wise

axis=1 → row-wise"""
"solution of task 3"
mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(np.mean(mat,axis=0))#prints col wise
print(np.mean(mat,axis=1))#row wise


