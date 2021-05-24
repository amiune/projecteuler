#!/usr/bin/env python
# coding: utf-8

# In[20]:


def divisorsSum(n):
    ret = 0
    for i in range(1, n-1):
        if n%i == 0:
            ret += i
    return ret


# In[21]:


N = 28123
abundants = []
for i in range(1,N+1):
    if divisorsSum(i) > i:
        abundants.append(i)


# In[22]:


sumOfAbundantsSet = set()
for i in abundants:
    for j in abundants:
        sumOfAbundantsSet.add(i+j)


# In[25]:


answer = 0 
for i in range(1, N+1):
    if i not in sumOfAbundantsSet:
        answer += i
    
print(answer)


# In[ ]:




