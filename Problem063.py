#!/usr/bin/env python
# coding: utf-8

# In[12]:


counter = 0
for n in range(1,100):
    for p in range(1, 100):
        np = n**p
        strnp = str(np)
        if p == len(strnp):
            print("{}^{} = {}".format(n,p,np))
            counter += 1
        if p > len(strnp): break
print(counter)


# In[ ]:




