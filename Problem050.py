#!/usr/bin/env python
# coding: utf-8

# In[36]:


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


# In[37]:


THRESHOLD = 1000000
answer = 2
primesSum = 2
i = 3
while primesSum + i < THRESHOLD:
    if isPrime(i):
        primesSum += i
        if isPrime(primesSum):
            answer = primesSum
    i += 2
    
i = 2
while primesSum > answer:
    if isPrime(i):
        primesSum -= i
        if isPrime(primesSum):
            answer = primesSum
    i += 1
    
print(answer)


# In[ ]:




