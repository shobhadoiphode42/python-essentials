#!/usr/bin/env python
# coding: utf-8

# In[1]:


a="hello"
print(a)


# In[2]:


b=""
print(b)


# In[3]:


a="satyamev jayte"
print(a)


# In[4]:


print(id(a))


# In[8]:


a="hello"
a[0]


# In[9]:


a


# In[10]:


a[1:3]


# In[11]:


a[::]


# In[12]:


a[:3]


# In[13]:


a[::2]


# In[14]:


a[::-1]


# In[15]:


len(a)


# In[16]:


help(string)


# In[17]:


str="HELLO"
str


# In[18]:


str.lower()


# In[19]:


len(str)


# In[20]:


str1="what we think we become"
str1.count("we")


# In[21]:


str1[0:15].count("we")


# In[22]:


str1.find("we")


# In[23]:


str1.rfind("we")


# In[24]:


str2="hello"
str2.upper()


# In[25]:


str2


# In[26]:


a=str2.upper()


# In[27]:


a


# In[28]:


str1


# In[29]:


str1.capitalize()


# In[30]:


str1.upper()


# In[31]:


str1.lower()


# In[32]:


str1.title()


# In[33]:


strr="HEllo"
strr.swapcase()


# In[34]:


str3="#####intel#$$$$"
str3.strip("#$")


# In[35]:


date1="16-12-2020"
date1[6:]


# In[37]:


date1.split("-")[-1]


# In[38]:


date1.split("-")[1]


# In[39]:


date1.split("-")[0]


# In[41]:


ip="192.168.10.1"
ip.split(".")[-1]


# In[44]:


ip.rsplit(".",1)


# In[45]:


str4="intel"
len(str4)


# In[46]:


str4.ljust(10,"#")


# In[48]:


list1=["sahil","ankur","hello"]
age=30
marks=90
for each in list1:
    print(each,age,marks)


# In[49]:


acc="8976543"
acc.rjust(10,"0")


# In[50]:


acc.zfill(10)


# In[51]:


bin(16)[2:].zfill(16)


# In[52]:


str5="#####int####el####"
str5.replace("#","")


# In[53]:


list1


# In[54]:


"/".join(list1)


# In[57]:


"123".isdigit()


# In[58]:


a=input("enter value")
if a.isdigit():
    a=eval(a)
print(a,type(a))


# In[59]:


"intel".isalpha()


# In[60]:


"intel87".isalpha()


# In[61]:


"intel34".isalnum()


# In[ ]:




