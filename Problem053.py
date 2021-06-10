#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[5]:


factorials = np.zeros((101))
factorials[0] = 1
for i in range(1,101):
    factorials[i] = i*factorials[i-1]


# In[11]:


counter = 0
for n in range(1,101):
    for r in range(1, n+1):
        combinations = factorials[n] / (factorials[r] * factorials[n-r])
        if combinations > 1_000_000:
            counter += 1
print(counter)


# In[ ]:




