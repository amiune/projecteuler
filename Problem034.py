#!/usr/bin/env python
# coding: utf-8

# In[17]:


from math import factorial

answer = 0
for i in range(10,factorial(9)):
    factorialSum = 0
    tmp = str(i)
    for j in range(len(tmp)):
        factorialSum += factorial(int(tmp[j]))
    if i == factorialSum:
        answer += i
        print(i)
        
print(answer)


# In[ ]:




