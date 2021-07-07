#!/usr/bin/env python
# coding: utf-8

# In[50]:


import math
from fractions import Fraction
#https://en.wikipedia.org/wiki/Pell%27s_equation


# In[90]:


def getContinuedFractionOfNumberSqrt(number, N):
    nsqrt = math.sqrt(number)
    coef = int(nsqrt)
    
    ret = []
    ret.append(coef)
    
    numerator1 = 1
    denominator1 = -coef 
    
    numerator2 = -denominator1 
    denominator2 = number - numerator2*numerator2 
    if denominator2 == 0: return ret
    
    coef3 = int(numerator1 * (nsqrt + numerator2)/denominator2)
    denominator3 = int(denominator2 / numerator1) 
    numerator3 = numerator2 - denominator3*coef3 
    
    periodCounter = 0
    coefsSet = set()
    for _ in range(N-1):
        periodCounter += 1
        coefsSet.add((coef3,numerator3,denominator3))
        
        ret.append(coef3)
        
        coef = coef3
        numerator1 = denominator3 
        denominator1 = numerator3 

        numerator2 = -denominator1
        denominator2 = number - numerator2*numerator2 
        if denominator2 == 0: return ret

        coef3 = int(numerator1 * (nsqrt + numerator2)/denominator2) 
        denominator3 = int(denominator2 / numerator1)
        numerator3 = numerator2 - denominator3*coef3 
        
    return ret


# In[91]:


def convergents(a):
    f = []
    f.append(Fraction(a[0],1))
    f.append(Fraction(a[0]*a[1] + 1, a[1]))
    for i in range(2,len(a)):
        f.append(Fraction(a[i]*f[i-1].numerator+f[i-2].numerator, a[i]*f[i-1].denominator+f[i-2].denominator))
    return f


# In[96]:


maxX = 0
answer = 0
for D in range(2,1000+1):
    if math.sqrt(D) == int(math.sqrt(D)): continue
    coefs = getContinuedFractionOfNumberSqrt(D,100)
    convs = convergents(coefs)
    for c in convs:
        x = c.numerator
        y = c.denominator
        v = x*x - D*y*y
        if v == 1:
            if x > maxX:
                maxX = x
                answer = D
                print("D:{} x:{} y:{}".format(D,x,y))
            break


# In[ ]:




