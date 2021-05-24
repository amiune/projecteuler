#!/usr/bin/env python
# coding: utf-8

# In[13]:


answer = 2
divisible = False
while not divisible:
    divisible = True
    for i in [3, 5, 7, 11, 13, 17, 19]:
        if answer % i != 0:
            divisible = False
            break
    if divisible:
        for i in range(1,21):
            if answer % i != 0:
                divisible = False
                break
    if divisible:
        break
    answer += 2
print(answer)


# In[ ]:




