#!/usr/bin/env python
# coding: utf-8

# In[4]:


distinctPowers = set()
for a in range(2,100+1):
    for b in range(2,100+1):
        tmp = a**b
        distinctPowers.add(tmp)
        
print(len(distinctPowers))
#print(sorted(distinctPowers))


# In[ ]:




