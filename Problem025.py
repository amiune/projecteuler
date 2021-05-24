#!/usr/bin/env python
# coding: utf-8

# In[3]:


f1 = 1
f2 = 1
fn = f1 + f2
index = 3
while len(str(fn)) < 1000:
    index += 1
    f1 = f2
    f2 = fn
    fn = f1 + f2

print(fn)
print(index)


# In[ ]:




