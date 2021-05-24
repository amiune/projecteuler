#!/usr/bin/env python
# coding: utf-8

# In[6]:


answer = 0
n = 2000000
notprimes = set()
for i in range(2, n+1):
    if i not in notprimes:
        answer += i
        for j in range(i*i, n+1, i):
            notprimes.add(j)
            
print(answer)


# In[ ]:




