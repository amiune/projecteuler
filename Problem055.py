#!/usr/bin/env python
# coding: utf-8

# In[43]:


def isPalindromeNumber(n):
    s = str(n)
    l = len(s)
    for i in range(int(l/2)):
        if s[i] != s[l-i-1]: return False
    return True


# In[44]:


def isLychrel(n):
    for it in range(50):
        n = n + int(''.join(reversed(str(n))))
        if isPalindromeNumber(n): return False
    return True


# In[46]:


answer = 0
for n in range(1,10000):
    if isLychrel(n): 
        answer += 1
print(answer)


# In[ ]:




