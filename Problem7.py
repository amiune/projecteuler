#!/usr/bin/env python
# coding: utf-8

# In[18]:


def isprime(x):
    for i in range(3,x,2):
        if x % i == 0:
            return False
    return True

n = 3
counter = 2
while counter < 10001:
    n += 2
    #print(str(n) + " " + str(isprime(n)))
    if isprime(n):
        #print(n, end=", ")
        counter += 1
    
    
print(n)


# In[ ]:




