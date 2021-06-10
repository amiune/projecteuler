#!/usr/bin/env python
# coding: utf-8

# In[20]:


for n in range(100,1000000):
    tmp = int('1'+str(n))
    tmpSortedStr = sorted(str(tmp))
    isGood = True
    for x in range(2,7):
        tmp2SortedStr = sorted(str(tmp * x))
        if tmp2SortedStr != tmpSortedStr:
            isGood = False
            break
    if isGood:
        print('1'+str(n))
        break


# In[ ]:




