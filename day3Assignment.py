#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = int(input("Enter the value of n: "))
sum=0
while num>0:
    sum=sum+num
    num=num-1
print("total=",sum)


# In[3]:


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




