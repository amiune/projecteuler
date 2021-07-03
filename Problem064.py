#!/usr/bin/env python
# coding: utf-8

# In[98]:


import math


# In[103]:


def getContinuedFractionPeriod(number):
    nsqrt = math.sqrt(number)
    coef = int(nsqrt)
    
    numerator1 = 1
    denominator1 = -coef # -4
    
    #print("({},{}/sqrt({}){})".format(coef,numerator1,number,denominator1))
    
    numerator2 = -denominator1 # 4
    denominator2 = number - numerator2*numerator2 # 23 - 4*4 = 23 - 16 = 7
    if denominator2 == 0: return 0
    
    #print("({}*(sqrt({})+{})/{})".format(numerator1,number,numerator2,denominator2))
    
    coef3 = int(numerator1 * (nsqrt + numerator2)/denominator2) # 1
    denominator3 = int(denominator2 / numerator1) # 7 / 1 = 7
    numerator3 = numerator2 - denominator3*coef3 # 4 - 7 = -3
    
    #print("({} + sqrt({}){}/{})".format(coef3,number,numerator3,denominator3))
    
    periodCounter = 0
    coefsSet = set()
    for _ in range(1000):
        periodCounter += 1
        coefsSet.add((coef3,numerator3,denominator3))
        
        coef = coef3
        numerator1 = denominator3 
        denominator1 = numerator3 
        
        #print()
        #print("({},{}/sqrt({}){})".format(coef,numerator1,number,denominator1))

        numerator2 = -denominator1
        denominator2 = number - numerator2*numerator2 
        if denominator2 == 0: return 0
        
        #print("({}*(sqrt({})+{})/{})".format(numerator1,number,numerator2,denominator2))

        coef3 = int(numerator1 * (nsqrt + numerator2)/denominator2) 
        denominator3 = int(denominator2 / numerator1)
        numerator3 = numerator2 - denominator3*coef3 
        
        #print("({} + sqrt({}){}/{})".format(coef3,number,numerator3,denominator3))
        if (coef3,numerator3,denominator3) in coefsSet: return periodCounter
        
    


# In[104]:


answer = 0
for n in range(2,10000+1):
    period = getContinuedFractionPeriod(n)
    if period % 2 != 0:
        answer += 1
print(answer)


# In[ ]:




