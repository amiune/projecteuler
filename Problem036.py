#!/usr/bin/env python
# coding: utf-8

# In[11]:


def isPalindrome(x):
    n = len(x)
    for i in range(int(n/2)):
        if x[i] != x[n-i-1]:
            return False
    return True


# In[17]:


answer = 0
for n in range(1000000):
    decimalStr = str(n)
    if isPalindrome(decimalStr):
        binaryStr = bin(n)[2:]
        if isPalindrome(binaryStr):
            answer += n

print(answer)


# In[ ]:




