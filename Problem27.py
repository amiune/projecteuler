#!/usr/bin/env python
# coding: utf-8

# In[6]:


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6. 
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True 


# In[7]:


def eratosthenes(n):
    primes = []
    multiples = []
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
    return primes

primes = eratosthenes(1000)
print(primes)
print(len(primes))


# In[11]:


bestCounter = 0
besta = -1
bestb = -1
for b in primes:
    for a in range(-b,b+1):
        counter = 0
        for n in range(0,80):
            tmp = n*n + a*n + b
            if not is_prime(tmp):
                break
            counter = n
        if counter > bestCounter:
            bestCounter = counter
            besta = a
            bestb = b

print(str(besta) + " " + str(bestb) + " -> " +str(bestCounter))
                


# In[12]:


print(besta*bestb)


# In[ ]:




