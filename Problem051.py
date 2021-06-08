#!/usr/bin/env python
# coding: utf-8

# In[151]:


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


# In[152]:


# 6 digits numbers
familyPositions = []
for i in range(1,2**5):
    indexesToChange = []
    for idx,pos in enumerate([1,2,4,8,16]):
        if i&pos != 0:
            indexesToChange.append(idx+2)
    familyPositions.append(indexesToChange)


# In[153]:


primes = []
for x in range(100000,1000000):
    if isPrime(x):
        primes.append(x)
print(len(primes))


# In[154]:


found = False
for prime in primes:
    for fp in familyPositions:
        if len(fp) >= 2:
            strNumber = str(prime)
            lenStrNumber = len(strNumber)
            if len(fp) == 2 and strNumber[lenStrNumber-fp[0]] != strNumber[lenStrNumber-fp[1]]: continue
            if len(fp) == 3 and (strNumber[lenStrNumber-fp[0]] != strNumber[lenStrNumber-fp[1]] or strNumber[lenStrNumber-fp[0]] != strNumber[lenStrNumber-fp[2]]): continue
            if len(fp) == 4 and (strNumber[lenStrNumber-fp[0]] != strNumber[lenStrNumber-fp[1]] or                                  strNumber[lenStrNumber-fp[1]] != strNumber[lenStrNumber-fp[2]] or                                  strNumber[lenStrNumber-fp[2]] != strNumber[lenStrNumber-fp[3]]): continue
        tmp = prime
        counter = 0
        for i in range(10):
            for pos in fp:
                #remove family position
                tmp = tmp - int((tmp % (10**pos))/(10**(pos-1)))*(10**(pos-1))
                #replace digit 
                tmp = tmp + i*10**(pos-1)
            if tmp >= 100000 and isPrime(tmp):
                counter += 1
        if counter >= 8:
            print("Prime: {}".format(prime))
            print("Family Positions: {}".format(fp))
            for i in range(10):
                for pos in fp:
                    #remove family position
                    tmp = tmp - int((tmp % (10**pos))/(10**(pos-1)))*(10**(pos-1))
                    #replace digit 
                    tmp = tmp + i*10**(pos-1)
                if isPrime(tmp):
                    print(tmp)
            found = True
            break
    if found: break


# In[ ]:




