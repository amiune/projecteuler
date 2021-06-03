#!/usr/bin/env python
# coding: utf-8

# In[6]:


def isPrime(n):
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


# In[9]:


def isPermutation(a,b):
    if len(a) == len(b):
        return sorted(a) == sorted(b)
    return False


# In[18]:


for n1 in range(1001,9999+1,2):
    if isPrime(n1):
        for diff in range(1,int(10000/3)):
            if isPermutation(str(n1),str(n1+diff)) and isPermutation(str(n1),str(n1+2*diff)):
                if isPrime(n1+diff) and isPrime(n1+2*diff):
                    print("{},{},{}".format(n1,n1+diff,n1+2*diff))


# In[ ]:




