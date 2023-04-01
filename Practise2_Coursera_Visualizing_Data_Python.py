#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([1,2,4,6,9])

print(type(a))


# In[3]:


print (a.shape)


# In[4]:


print(a[1], a[3])


# In[5]:


b = np.array([[1,2],[3,4]])


# In[6]:


print(b.shape)


# In[7]:


print(b[0,0], b[0,1], b[1,1])


# In[8]:


c = np.array([[1,2],[3,4],[5,6]])


# In[9]:


print(c.shape)


# In[10]:


print(c[0,1], c[1,0], c[2,0], c[2,1])


# In[11]:


d = np.zeros((2,3))


# In[12]:


print(type(d))


# In[15]:


print(d.shape)
print(d)


# In[16]:


e = np.ones((4,2))
print(e.shape)
print(e)


# In[17]:


f = np.full((2,2), 9)
print(f.shape)

print(f)


# In[19]:


g = np.random.random((3,3))
print(g.shape)
print(g)


# In[ ]:




