#!/usr/bin/env python
# coding: utf-8

# In[80]:


from fractions import Fraction


# In[81]:


eCoefs = [0,2,1]
for i in range(1,100):
    eCoefs.append(2*i)
    eCoefs.append(1)
    eCoefs.append(1)


# In[82]:


N = 100
f = eCoefs[N]
for i in range(N-1,0,-1):
    f = eCoefs[i] + Fraction(1,f)
print("{}/{}".format(f.numerator,f.denominator))


# In[83]:


s = str(f.numerator)
answer = 0
for c in s:
    answer += int(c)
print(answer)


# In[ ]:




