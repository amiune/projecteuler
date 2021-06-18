#!/usr/bin/env python
# coding: utf-8

# In[4]:


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


# In[15]:


diagNumber = 1
increment = 2
primesCounter = 0
diagonalCounter = 1
while True:
    for i in range(4):
        diagNumber = diagNumber + increment
        if isPrime(diagNumber): primesCounter += 1
    diagonalCounter += 4
    if primesCounter / diagonalCounter < 0.10: break
    increment += 2
    
print(increment+1)


# In[ ]:




