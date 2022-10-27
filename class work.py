#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x=numpy.mean(speed)
print(x)


# In[2]:


import numpy
speed =[99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)


# In[3]:


from scipy import stats
speed =[99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)


# In[4]:


import numpy 
speed =[32,111,138,28,59,77,97]
x=numpy.std(speed)
print(x)


# In[5]:


import numpy
speed =[32,111,138,28,59,77,97]
x=numpy.var(speed)
print(x)


# In[ ]:




