#!/usr/bin/env python
# coding: utf-8

# In[57]:


def divisorsSum(n):
    ret = 0
    for i in range(1, n-1):
        if n%i == 0:
            ret += i
    return ret


# In[58]:


import numpy as np
N = 10000
divisors = np.zeros((N)).astype(int)
for i in range(1,N):
    divisors[i] = divisorsSum(i)


# In[59]:


answer = 0
for i in range(1,N):
    if divisors[i] < N and i == divisors[divisors[i]] and i != divisors[i]:
        answer += i
print(answer)


# In[ ]:




