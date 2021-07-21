#!/usr/bin/env python
# coding: utf-8

# In[15]:


f = open("p067_triangle.txt", "r")
triangle = []
for line in f:
    triangle.append(line.replace("\n",""))


# In[19]:


n = len(triangle)


# In[20]:


import numpy as np
t = np.zeros((n,n))


# In[21]:


for i in range(n):
    s = triangle[i].split()
    for j in range(len(s)):
        t[i,j] = int(s[j])


# In[22]:


for i in range(1,n):
    for j in range(i+1):
        if j-1 < 0:
            t[i,j] += t[i-1,j]
        else:
            t[i,j] = np.maximum(t[i,j] + t[i-1,j], t[i,j] + t[i-1,j-1])


# In[24]:


int(np.max(t[n-1,:]))


# In[ ]:




