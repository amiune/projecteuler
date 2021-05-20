#!/usr/bin/env python
# coding: utf-8

# In[11]:


#the slow one, I used this to find the series
from collections import deque
for N in range(10):
    paths = deque([(0,0)])
    pathsCounter = 0
    while len(paths) > 0:
        tmp = paths.popleft()
        row, col = tmp
        if row == N and col == N:
            pathsCounter += 1
        if row + 1 < N+1:
            paths.append((row + 1, col))
        if col + 1 < N+1:
            paths.append((row, col + 1))

    print(str(N) + "-> " + str(pathsCounter))


# In[28]:


#pascal triangle
import numpy as np
N = 20
pascalt = np.ones((N+1,N+1))
for i in range(1,N+1):
    for j in range(1,N+1):
        pascalt[i,j] = pascalt[i,j-1] + pascalt[i-1,j]
print(int(pascalt[N,N]))


# In[ ]:




