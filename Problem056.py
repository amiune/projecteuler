#!/usr/bin/env python
# coding: utf-8

# In[1]:


answer = 0
for a in range(1,100):
    for b in range(1,100):
        digitalSum = 0
        s = str(a**b)
        for c in s:
            digitalSum += int(c)
        answer = max(answer, digitalSum)
print(answer)


# In[ ]:




