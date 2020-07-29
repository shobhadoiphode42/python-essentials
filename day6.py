#!/usr/bin/env python
# coding: utf-8

# In[1]:


d1={"i":"IBM","d":"dog","i":"infosis"}
print(d1)


# In[3]:


del d1["i"]


# In[4]:


print(d1)


# In[5]:


d1["i"]="infosys"
print(d1)


# In[6]:


d1["i"]="infosys company"
print(d1)


# In[7]:


d2=d1.copy()
print(d2)


# In[9]:


print(d1["d"])


# In[13]:


k=eval(input("Enter the key"))
print(d1.get(k,"Not"))


# In[14]:


d1.pop('d')


# In[15]:


d2


# In[16]:


d1.update(d2)


# In[17]:


d1


# In[18]:


d1.keys()


# In[19]:


d1.values()


# In[21]:


d1.items()


# In[22]:


for k,v in list(d1.items()):
    if k=='i':
        del d1[k]
    print(k,v)


# In[24]:


list1=[1,2,3,4,5]
print([each**2 for each in list1])


# In[32]:


try:
    val=int(input("Enter the number"))
    d1=100
    c=d1/val
    print(c)
except Exception as e:
    print(e)
else:
    print("no error occured")
finally:
    print("done")
    


# In[ ]:




