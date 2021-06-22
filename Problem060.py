#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from itertools import combinations


# In[ ]:


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


# In[ ]:


# Small sets (3,7), (3,11), (3,17), ...  
possibleSmallPairs = []
for i in range(4993, 10000, 2):
    for j in range(i+2, 10000):
        if isPrime(i) and isPrime(j):
            if isPrime(int(str(i) + str(j))) and isPrime(int(str(j) + str(i))):
                possibleSmallPairs.append((i,j))
            
print(len(possibleSmallPairs))


# In[ ]:


minSum = 48553
for pair in possibleSmallPairs:
    print(pair)
    p1, p2 = pair
    possiblePrimes = []
    for i in range(11, minSum, 2):
        if isPrime(i):
            if isPrime(int(str(i) + str(p1))) and isPrime(int(str(i) + str(p2))) and isPrime(int(str(p1) + str(i))) and isPrime(int(str(p2) + str(i))):
                possiblePrimes.append(i)

    for c in combinations(possiblePrimes,3):
        if p1 + p2 + c[0] + c[1] + c[2] > minSum: continue
        if isPrime(int(str(c[0]) + str(c[1]))) and isPrime(int(str(c[1]) + str(c[0])))         and isPrime(int(str(c[0]) + str(c[2]))) and isPrime(int(str(c[2]) + str(c[0])))         and isPrime(int(str(c[1]) + str(c[2]))) and isPrime(int(str(c[2]) + str(c[1]))):
            print("{}, {}, {}, {}, {}".format(p1, p2, c[0],c[1],c[2]))
            tmpSum = p1 + p2 + c[0] + c[1] + c[2]
            print(tmpSum)
            minSum = tmpSum


# In[ ]:


#5197, 5701, 13, 6733, 8389
#26033


# In[ ]:





# In[ ]:




