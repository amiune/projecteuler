#!/usr/bin/env python
# coding: utf-8

# In[2]:


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True 


# In[11]:


circulars = [2]
for i in range(3,1000000,2):
    if is_prime(i):
        isCircular = True
        tmp = str(i)
        for j in range(len(tmp)-1):
            tmp = tmp[-1:] + tmp[:-1]
            if not is_prime(int(tmp)):
                isCircular = False
                break
        if isCircular:
            circulars.append(i)
            
print(circulars)


# In[12]:


len(circulars)


# In[ ]:




