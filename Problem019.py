#!/usr/bin/env python
# coding: utf-8

# In[17]:


from datetime import date
from datetime import timedelta


# In[18]:


start = date.fromisoformat('1901-01-01')
end = date.fromisoformat('2000-12-31')


# In[19]:


day = timedelta(days=1)


# In[20]:


counter = 0
while start <= end:
    if start.day == 1 and start.isoweekday() == 7:
        counter += 1
    start += day


# In[21]:


counter


# In[ ]:




