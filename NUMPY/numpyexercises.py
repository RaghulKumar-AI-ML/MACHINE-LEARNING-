import numpy as np
arr = np.arange(0,10)
print(arr)

arr2=np.array([[2,3,4],
               [5,6,7]])
"""
print(arr2)
print(arr2.shape)
print(type(arr2))
print(arr2.dtype)
print(arr2.ndim)
print(arr2.reshape(1,6))
"""
"""print(arr2[1,1])
print(arr2[:,1])
print(arr2[0,:])
print(arr2[0:2,1:3])
arr2[0,0]=20
print(arr2)
"""
result = sum(arr2)/len(arr2)
print(result)
result2 = np.mean(arr2)
print(result2)
standard=np.std(arr)
print(standard)
dott=np.dot(arr,arr)
print(dott)