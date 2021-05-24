#!/usr/bin/env python
# coding: utf-8

# In[6]:


answer = 2
maxCounter = 1
for i in range(3,1000000):
    tmp = i
    counter = 1
    while tmp > 1:
        if tmp % 2 == 0:
            tmp = int(tmp / 2)
        else:
            tmp = 3 * tmp + 1
        counter += 1
    if counter > maxCounter:
        maxCounter = counter
        answer = i
    
print(maxCounter)
print(answer)


# In[ ]:




