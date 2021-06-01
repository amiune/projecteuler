#!/usr/bin/env python
# coding: utf-8

# In[6]:


def eratosthenes(n):
    primes = []
    multiples = []
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
    return primes

primes = eratosthenes(10000)


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


# In[10]:


for odd in range(3,10000,2):
    if not isPrime(odd):
        found = False
        for p in primes:
            if p >= odd or found: break
            for s in range(1,100):
                tmp = p + 2 * (s*s)
                if tmp > odd: break
                if tmp == odd:
                    found = True
                    #print("{} = {} + 2 * {}^2".format(odd,p,s))
        if not found:
            print("{} NOT FOUND".format(odd))


# In[ ]:





# In[ ]:




