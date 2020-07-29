#!/usr/bin/env python
# coding: utf-8

# In[2]:


def func1(a,b):
    c=a+b
    print(c)
func1(10,20)


# In[3]:


def func1(a,b):
    c=a+b
    return c
res=func1(10,20)+10
print(res)


# In[8]:


def func1(name,age=30, marks=60):
    print(name,age,marks)
func1("abc",20,80)
func1("xyz")


# In[12]:


def fun1(a,*args):
    print(a,args)
fun1(12)
fun1(10,20)
fun1(4,5,1,6,9,4)


# In[14]:


def fun1(**kwargs):
    print(kwargs)
fun1(name="xyz",marks=70)


# def fun2(list1):
#     print("inside before appending", list1, id(list1))
#     list1.append(30)
#     print("After appending", list1, id(list1))
# list2=[4,5,6]
# fun2(list2)
# print("after calling",list2,id(list2))

# In[19]:


def fun2(list1):
    print("inside before appending", list1, id(list1))
    list1.append(30)
    print("After appending", list1, id(list1))
list2=[4,5,6]
fun2(list2)
print("after calling",list2,id(list2))


# In[20]:


def fun1(a):
    print("before",a)
    a=a+10
    print("after",a)
a=30
fun1(a)
print("After append",a)


# In[ ]:




