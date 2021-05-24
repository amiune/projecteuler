#!/usr/bin/env python
# coding: utf-8

# In[10]:


x = 1
for i in range(1000):
    x *= 2
s = str(x)
answer = 0
for i in range(len(s)):
    answer += int(s[i])
print(answer)


# In[ ]:




