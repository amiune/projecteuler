#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import numpy as np


# In[3]:


def phi(n):
    result = n
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            while n % i == 0: n /= i
            result -= result / i
    if n > 1: result -= result / n
    return result


# In[18]:


def phi_1_to_n(n):
    phi = np.zeros(n+1,dtype=int)
    phi[0] = 0
    phi[1] = 1
    for i in range(2,n+1): phi[i] = i;

    for i in range(2,n+1):
        if phi[i] == i:
            for j in range(i,n+1,i):
                phi[j] -= phi[j] / i
                
    return phi


# In[19]:


N = 10**7
phi = phi_1_to_n(N)


# In[20]:


def isPermutation(a,b):
    aDigits = np.zeros(10,dtype=int)
    bDigits = np.zeros(10,dtype=int)
    for c in a: aDigits[int(c)] += 1
    for c in b: bDigits[int(c)] += 1
    for i in range(10): 
        if aDigits[i] != bDigits[i]: return False
    return True


# In[28]:


answer = 0
minRatio = 1000000000
for n in range(2, N):
    tmp = n/phi[n]
    if tmp < minRatio:
        if isPermutation(str(int(n)), str(int(phi[n]))):
            minRatio = tmp
            answer = n
print(answer)


# In[ ]:




