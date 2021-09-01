#!/usr/bin/env python
# coding: utf-8

# In[4]:


from fractions import Fraction


# In[43]:


N = 1
D = 1000000
threshold = Fraction(3,7) #0.42857142857142855

#Don't do this at home :)
answer = Fraction(1,D)
for d in range(1,D+1):
    for n in range(int(d*0.428570),int(d*0.42859)):
        tmp = Fraction(n,d)
        if tmp >= threshold: continue
        if tmp > answer: answer = tmp
                
print(answer)


# In[ ]:




