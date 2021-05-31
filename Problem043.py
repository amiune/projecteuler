#!/usr/bin/env python
# coding: utf-8

# In[1]:


from itertools import permutations


# In[22]:


numbers = [0,1,2,3,4,5,6,7,8,9]
primes = [2,3,5,7,11,13,17]

answer = 0
counter = 0
for p in permutations(numbers):
    if p[0] > 0:
        tmp = "".join(str(x) for x in p)
        ok = True
        for i in range(1,8):
            tmp2 = int(tmp[i:i+3])
            if tmp2 % primes[i-1] != 0:
                ok = False
                break
        if ok: 
            print(tmp)
            counter += 1
            answer += int(tmp)

print(counter)
print(answer)


# In[ ]:




