#!/usr/bin/env python
# coding: utf-8

# In[15]:


f = open("p022_names.txt", "r")
s = sorted(f.read().replace('"','').split(","))


# In[21]:


answer = 0
for i in range(len(s)):
    charsum = 0
    for j in range(len(s[i])):
        charsum += ord(s[i][j]) - ord('A') + 1
    answer += charsum * (i+1)

print(answer)


# In[ ]:




