#!/usr/bin/env python
# coding: utf-8

# In[23]:


answer = -1
N = 1001
actualNumber = 1
actualIncrement = 1
while actualNumber <= N*N:
    for j in range(2):
        if actualNumber % 2 != 0:
            answer += actualNumber
        else:
            answer += actualNumber-1
        actualNumber += actualIncrement
    actualIncrement += 1
print(answer)


# In[ ]:




