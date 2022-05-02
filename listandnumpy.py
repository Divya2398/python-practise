import numpy as np
import time
import sys
# numpy operations
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)
print(a)
print(a.itemsize)

# compare list and numpy (in terms of memory and execution time)
b = range(500)
print(sys.getsizeof(5)*len(b)) #14000-size

c = np.arange(500)
print(c.size*c.itemsize) #2000-size
sec= time.time()
list1 = range(50000)
list2 = range(50000)
result = [(x,y )for x,y in zip(list1, list2)]
print((time.time()-sec)*1000)

sec= time.time()
a1= np.arange(50000)
a2= np.arange(50000)
result2= a1 + a2
print((time.time()-sec)*1000)

s= np.array([3.14, 3, 4, 5, 6, 7]),
print(s)
p= np.array([2, 4, 5, 3.14] , dtype = int)
print(p)




