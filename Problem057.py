#!/usr/bin/env python
# coding: utf-8

# In[35]:


from fractions import Fraction


# In[36]:


def SqrtContinuedFraction(n):
    if n == 0: return Fraction(1,2) 
    return Fraction(1, 2 + SqrtContinuedFraction(n-1))


# In[38]:


answer = 0
for n in range(1001):
    f = Fraction(1,1) + SqrtContinuedFraction(n)
    if len(str(f.numerator)) > len(str(f.denominator)): answer += 1
print(answer)


# In[ ]:




