#!/usr/bin/env python
# coding: utf-8

# In[21]:


answer = 0
for i in range(100,1000):
    for j in range(100,1000):
        product = i * j
        s = str(product)
        palindrome = True
        for k in range(int(len(s)/2)):
            if s[k] != s[len(s)-k-1]:
                palindrome = False
                break
        if palindrome and product > answer:
            answer = product
print(answer)


# In[ ]:




