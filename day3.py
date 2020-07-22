#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10
b=10.2
type(a)


# In[2]:


j=90
i=float(j)


# In[3]:


print(i
     )


# In[4]:


k=10.3
l=int(k)
print(l)


# In[5]:


a='34'
b=str(a)
print(a)


# In[6]:


type(b)


# In[7]:


m=123456789012345678.23
print(m)


# In[8]:


a=input("Enter the value")
print(a)


# In[10]:


a=int(input("Enter the value"))
r=a+10
print(r)


# In[11]:


a=float(input("Enter the value"))
r=a+10.12
print(r)


# In[12]:


a=eval(input("Enter the value"))
r=a+"10.12"
print(r)


# In[13]:


hello="hi"
a=eval(input("Enter the value"))
r=a+"10.12"
print(r)


# In[14]:


eval('10')


# In[15]:


eval("10+20+90")


# In[16]:


pass1=input("Enter password")
if pass1=="hello":
    print("Welcome Hello")
print("Done")


# In[17]:


pass1=input("Enter password")
if pass1=="hello":
    print("Welcome Hello")
else:
    print("Wrong passworsd")


# In[20]:


num=eval(input("Enter marks"))
print(num)
grade=""
if num>=90:
    grade="A"
elif num>=80:
    grade="B"
elif num>=70:
    grade="C"
elif num>=60:
    grade="D"
else:
    grade="E"
print(f"The marks is{num} and grade is{grade}")


# In[21]:


print(type(range(10)))


# In[22]:


help(range)


# In[23]:


range(10)


# In[24]:


list(range(10))


# In[25]:


list(range(1,10,2))


# In[28]:


list(range(5,-22,-2))


# In[30]:


for each in range(10):
    print(each,end=",")


# In[31]:


str="pythonprogramming"
for each in str:
    print(each,end="")


# In[32]:


list=[1,2,3,4,5]
for each in list:
    print(each)


# In[37]:


sum=0
for each in range(1,11):
    sum=sum+each
    print(each,"-",sum)
print("sum of number is",sum)


# In[38]:


pass1=input("Enter pass1")
while pass1!="hello":
    print("Wrong password")
    pass1=input("Enter password again")
print("Welocme")


# In[39]:


sum1=0
while True:
    num=int(input("Enter the number"))
    sum1=sum1+num
    print(sum1)
    if num==0:
        break
print("Final sum is ",sum1)


# In[40]:


sum1=0
flag=1
while flag:
    num=int(input("Enter the number"))
    sum1=sum1+num
    print(sum1)
    if num==0:
        flag=0
print("Final sum is ",sum1)


# In[41]:


str="theAvengers"
for each in str:
    print(each)


# In[42]:


str="theAvengers"
for each in str:
    if each=="A":
        break
    print(each)
    


# In[43]:


list=[1,2,"a",3,4,5]
for each in list:
    print(each)


# In[44]:


list=["a","b","c","d"]
for each in list:
    if each=="c":
        continue
    print(each)


# In[45]:


num=10
sum=0
while(num>0):
    sum+=num
    num-=1
print("the sum is ",sum)


# In[46]:


num = int(input("Enter the value of n: "))
sum=0
while num>0:
    sum=sum+num
    num=num-1
print("total=",sum)


# In[51]:


Number = int(input(" Please Enter any Number: "))
count = 0

for i in range(2, (Number//2 + 1)):
    if(Number % i == 0):
        count = count + 1
        break

if (count == 0 and Number != 1):
    print(" %d is a Prime Number" %Number)
else:
    print(" %d is not a Prime Number" %Number)


# In[ ]:




