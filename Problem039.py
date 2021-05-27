#!/usr/bin/env python
# coding: utf-8

# In[1]:


# a + b + c = p
# a^2 + b^2 = c^2

# D = p - a
# E = a^2


# In[12]:


bestP = 0
maxCounter = 0
for p in range(1,1001):
    counter = 0
    for a in range(1,p):
        D = p - a
        E = a**2

        c = (E + D**2)/(2.0*D)
        b = D - c
        if b > 0 and a <= b and float(int(c)) == c:
            counter += 1
    if counter > maxCounter:
        bestP = p
        maxCounter = counter
        
        
print(bestP)


# In[ ]:




