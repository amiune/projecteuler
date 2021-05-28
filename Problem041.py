#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[25]:


from itertools import permutations
answer = 0
for n in range(4,10):
    nNumbers = list(range(1,n+1))
    for p in permutations(nNumbers):
        number = 0
        for i in range(n):
            number += p[n-i-1] * (10**i)
        if isPrime(number) and number > answer:
            answer = number
            
print(answer)


# In[ ]:




