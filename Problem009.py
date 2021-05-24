#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[8]:


n = 1000
for a in range(1,n-2):
    for b in range(a+1, n-1):
        c = math.sqrt(a*a + b*b)
        if a + b + c == 1000:
            print(int(a*b*c))
            break


# In[ ]:




