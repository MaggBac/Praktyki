#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=(2.3 * 3.0) - 6.9
b=(3.45 * 2.0) - 6.9
c=(3.45 * 3.0) - 10.35
print(a)
print(b)
print(c)


# In[2]:


a=(2.3 * 3.0) - 6.9
b=(3.45 * 2.0) - 6.9
c=(3.45 * 3.0) - 10.35
print(float(a))
print(float(b))
print(float(c))


# In[3]:


a=round((2.3 * 3.0) - 6.9)
b=round((3.45 * 2.0) - 6.9)
c=round((3.45 * 3.0) - 10.35)
print(a)
print(b)
print(c)


# In[4]:


a=round(2.3 * 3.0) - 6.9
b=round(3.45 * 2.0) - 6.9
c=round(3.45 * 3.0) - 10.35
print(a)
print(b)
print(c)


# In[5]:


a=(2.3 * 3.0) == 6.9
b=(3.45 * 2.0) == 6.9
c=(3.45 * 3.0) == 10.35
print(a)
print(b)
print(c)


# In[6]:


list=[((2.3 * 3.0) - 6.9),((3.45 * 2.0) - 6.9),((3.45 * 3.0) - 10.35)]
def count(numbers):
    i=0
    for i in numbers:
        print(round(float(i)))
        i+=1
count(list)


# In[7]:


a=(2.3 * 3.0) - 6.9
b=(3.45 * 2.0) - 6.9
c=(3.45 * 3.0) - 10.35
print(format(a,".2f"))
print(format(b,".2f"))
print(format(c,".2f"))


# In[8]:


from decimal import *
getcontext().prec=6
a=Decimal(2.3 * 3.0) - Decimal(6.9)
b=(3.45 * 2.0) -(6.9)
c=Decimal(3.45 * 3.0) - Decimal (10.35)
print('Expected:',0,sep='\n')
print('Achived:',a,sep='\n')
print(b)
print(c)


# In[ ]:




