#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


def isPentagonal(x):
    r = (1+np.sqrt(1+24*x))/6
    if abs(int(r) - r) < 0.0000001: return True
    return False


# In[6]:


def isHexagonal(x):
    r = (1+np.sqrt(1+8*x))/4
    if abs(int(r) - r) < 0.0000001: return True
    return False


# In[14]:


n = 286
while True:
    triangle = n*(n+1)/2
    if isPentagonal(triangle) and isHexagonal(triangle):
        print(int(triangle))
        break
    n += 1


# In[ ]:




