#!/usr/bin/env python
# coding: utf-8

# In[1]:


from itertools import permutations


# In[43]:


p = permutations(range(10))


# In[44]:


nperm = None
for i in range(1000000):
    nperm = next(p)

print(nperm)


# In[50]:


print(''.join(str(i) for i in nperm))


# In[ ]:




