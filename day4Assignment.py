#!/usr/bin/env python
# coding: utf-8

# In[2]:


str1 = "What we think we become; we are a python programmer"
sub = "we" 
print("The original string is : " + str1)  
print("The substring to find : " + sub)   
res = [i for i in range(len(str1)) if str1.startswith(sub, i)]  
print("The start indices of the substrings are : " + str(res)) 


# In[4]:


str2="HELLO"
print(str2)
str2.islower()


# In[6]:


str2="hello"
print(str2)
str2.isupper()


# In[ ]:




