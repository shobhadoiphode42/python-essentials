#!/usr/bin/env python
# coding: utf-8

# In[1]:


tup1=()
print(tup1,(type(tup1)))


# In[3]:


tup2=(1,)
print(tup2,(type(tup2)))


# In[4]:


tup3=(1,2,3,"a","hello")
print(tup3)


# In[5]:


tup4=1,2,3,"a"
print(tup4)


# In[6]:


tup4[0]


# In[7]:


A=("iron-man","thor","hulk","captain")
A[1]


# In[8]:


tup6=(10,20)
print(tup6)


# In[10]:


a,b=tup6
print(a)
print(b)


# In[11]:


a,b,*c=(10,20,30,40)
print(a,b,c)


# In[12]:


A[::-1]


# In[15]:


t1=(1,2,3,4,5,6,7,8,9,1,2,3,4)
print(t1)


# In[16]:


t1.count(4)


# In[17]:


t1.index(4)


# In[18]:


t2=(10,20)


# In[19]:


t1+t2


# In[20]:


min(t1)


# In[21]:


max(t1)


# In[22]:


list1=[1,2,3]
t1=tuple(list1)
print(t1)


# In[23]:


a=input("Enter value")
t1=tuple(a.split()  )
print(t1)


# In[24]:


list1=[]
print(list1,type(list1))


# In[26]:


list2=[1,2,3,4,"a",("d",1)]
print(list2)


# In[27]:


list2[-1]


# In[30]:


list2[::-1]


# In[31]:


list4=[1,2,("hello","iron-man"),"m"]
print(list4)


# In[32]:


list4[2][1]


# In[33]:


list4[2][1][5:]


# In[34]:


list4


# In[35]:


list4[2]="s"


# In[36]:


list4


# In[38]:


list5=list4[:]
print(list5)


# In[39]:


[10,20]+[30,40]


# In[40]:


[10,20]*2


# In[41]:


A


# In[42]:


A=['iron-man', 'thor', 'hulk', 'captain']
print(A)


# In[43]:


A.append("vision")


# In[44]:


a


# In[45]:


A


# In[46]:



A.extend("ahgsdg")


# In[47]:


A


# In[48]:


A1=['iron-man', 'thor', 'hulk', 'captain']
print(A1)


# In[49]:


A1.insert(1,"caption")


# In[50]:


A1


# In[53]:


A1.remove("caption")


# In[54]:


A1


# In[55]:


A1.pop(-1)


# In[56]:


A1


# In[57]:


A2=[1,2,3,4,5]


# In[58]:


A2.reverse()


# In[59]:


A2


# In[61]:


list8=[1,2,9,10,3,4,5,6,7]


# In[64]:


list8.sort(reverse=1)


# In[65]:


list8


# In[66]:


list7=[('k',10),('b',5),('c',10),('d',6),('e',20)]
print(list7)


# In[68]:


list7=[(2,10),(3,5),(9,10),(8,6),(1,20)]
def fun1(x):
    return(x[0]+x[1])
list7.sort(key=fun1)
print(list7)


# In[ ]:




