#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np


# In[2]:


def phi(n):
    result = n
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            while n % i == 0: n /= i
            result -= result / i
    if n > 1: result -= result / n
    return result


# In[3]:


def phi_1_to_n(n):
    phi = np.zeros(n+1)
    phi[0] = 0
    phi[1] = 1
    for i in range(2,n+1): phi[i] = i;

    for i in range(2,n+1):
        if phi[i] == i:
            for j in range(i,n+1,i):
                phi[j] -= phi[j] / i
                
    return phi


# In[4]:


N = 1000000
answer = 0
maximum = 0
phi = phi_1_to_n(N)
for n in range(1,N):
    tmp = n/phi[n]
    if tmp > maximum:
        answer = n
        maximum = tmp
print(answer)


# In[ ]:




