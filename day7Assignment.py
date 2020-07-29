#!/usr/bin/env python
# coding: utf-8

# In[1]:


port1 = {21:"FTP",22:"SSH",23:"telnet",80:"http"} 
port2 ={value:key for key,value in port1.items()}
print("The output:",port2)


# In[2]:


list1=[(1,2),(3,4),(5,6),(4,5)]
res=[]
for each in range(0,len(list1)):
    a,b=list1[each]
    res.append(a+b)
print(res)


# In[3]:


list1=[(1,2,3),[1,2],['a','hit','less']]
list2=[]
list2=[i for each in list1 for i in each]
print (list2)


# In[ ]:




