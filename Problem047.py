#!/usr/bin/env python
# coding: utf-8

# In[6]:


from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


# In[7]:


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


# In[8]:


def countPrimes(xlist):
    counter = 0
    for x in xlist:
        if isPrime(x):
            counter += 1
    return counter


# In[16]:


for n in range(1,1000000):
    if countPrimes(factors(n)) == 4     and countPrimes(factors(n+1)) == 4     and countPrimes(factors(n+2)) == 4     and countPrimes(factors(n+3)) == 4  :
        print(n)
        break
    


# In[ ]:




