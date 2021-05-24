#!/usr/bin/env python
# coding: utf-8

# In[9]:


N = 5
answer = 0
for i in range(10, N * (9**N)):
    tmp = str(i)
    powersSum = 0
    for digit in tmp:
        x = int(digit)
        powersSum += x**N
    if i == powersSum:
        print(i)
        answer += i
print(answer)


# In[ ]:




