#!/usr/bin/env python
# coding: utf-8

# In[3]:


N = 100
factorial = 1
for i in range(2, N+1):
    factorial *= i
print(factorial)


# In[4]:


answer = 0
s = str(factorial)
for i in range(len(s)):
    answer += int(s[i])

print(answer)


# In[ ]:




