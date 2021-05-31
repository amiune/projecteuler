#!/usr/bin/env python
# coding: utf-8

# In[128]:


import numpy as np


# In[129]:


def isPentagonal(x):
    r = (1+np.sqrt(1+24*x))/6
    if abs(int(r) - r) < 0.0000001: return True
    return False


# In[130]:


N=3000
for j in range(1,N):
    for k in range(j+1,N):
        pj = (3*j*j - j) / 2
        pk = (3*k*k - k) / 2
        if isPentagonal(pj+pk) and isPentagonal(pk-pj):
            print("{},{}".format(j,k))
            print("{},{}".format(pj,pk))
            print("D = {}".format(int(pk-pj)))
            break


# In[ ]:




