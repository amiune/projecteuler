#!/usr/bin/env python
# coding: utf-8

# In[8]:


answer = 2
f1 = 1
f2 = 2
f3 = f1 + f2
while(f3 <= 4000000):
    print(f3)
    if f3 % 2 == 0:
        answer += f3
    f1 = f2
    f2 = f3
    f3 = f1 + f2
print(answer)


# In[ ]:




