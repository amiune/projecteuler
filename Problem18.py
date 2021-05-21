#!/usr/bin/env python
# coding: utf-8

# In[16]:


triangle = ["75",
"95 64",
"17 47 82",
"18 35 87 10",
"20 04 82 47 65",
"19 01 23 75 03 34",
"88 02 77 73 07 63 67",
"99 65 04 28 06 16 70 92",
"41 41 26 56 83 40 80 70 33",
"41 48 72 33 47 32 37 16 94 29",
"53 71 44 65 25 43 91 52 97 51 14",
"70 11 33 28 77 73 17 78 39 68 17 57",
"91 71 52 38 17 14 91 43 58 50 27 29 48",
"63 66 04 68 89 53 67 30 73 16 69 87 40 31",
"04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"]


# In[17]:


n = len(triangle)


# In[18]:


import numpy as np
t = np.zeros((n,n))


# In[19]:


for i in range(n):
    s = triangle[i].split()
    for j in range(len(s)):
        t[i,j] = int(s[j])


# In[20]:


t


# In[21]:


for i in range(1,n):
    for j in range(i+1):
        if j-1 < 0:
            t[i,j] += t[i-1,j]
        else:
            t[i,j] = np.maximum(t[i,j] + t[i-1,j], t[i,j] + t[i-1,j-1])
t


# In[24]:


int(np.max(t[14,:]))


# In[ ]:




