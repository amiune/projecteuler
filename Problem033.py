#!/usr/bin/env python
# coding: utf-8

# In[2]:



for numerator in range(10,100):
    for denominator in range(numerator+1,100):
        if numerator % 10 != 0 and denominator % 10 != 0:
            division1 = numerator / denominator
            strNumerator = str(numerator)
            strDenominator = str(denominator)
            division2 = -1
            if strNumerator[1] == strDenominator[0]:
                division2 = float(strNumerator[0]) / float(strDenominator[1])
                if division1 == division2:
                    print(strNumerator + " / " + strDenominator)
                    print(strNumerator[0] + " / " + strDenominator[1])


# In[4]:


print(str(16*19*26*49) + " / " + str(64*95*65*98))


# In[3]:


print(str(1*1*2*4) + " / " + str(4*5*5*8))


# In[5]:


print(100) #answer


# In[ ]:




