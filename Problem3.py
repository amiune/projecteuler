#!/usr/bin/env python
# coding: utf-8

# In[20]:


from math import sqrt

def isPrime(number):
    return all(number % i for i in range(2,int(sqrt(number)+1)))

N = 600851475143
largestPrimeFactor = 2

while N != 1:
    if N % largestPrimeFactor == 0:
        N = N / largestPrimeFactor
    else:
        for i in range(largestPrimeFactor + 1, int(N)+1):
            if isPrime(i):
                largestPrimeFactor = i
                break

print(largestPrimeFactor)


# In[ ]:





# In[ ]:




