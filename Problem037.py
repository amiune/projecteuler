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


# In[6]:


answer = 0
for n in range(11,1000000,2):
    if isPrime(n):
        strN = str(n)
        truncatablePrime = True
        for i in range(1, len(strN)):
            if not isPrime(int(strN[i:])) or not isPrime(int(strN[:-i])):
                truncatablePrime = False
                break
        if truncatablePrime:
            answer += n
            print(n)
    
print(answer)


# In[ ]:




