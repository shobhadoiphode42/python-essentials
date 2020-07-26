#!/usr/bin/env python
# coding: utf-8

# In[4]:


def sorting(arr, n): 
    count = 0    
    for i in range(n): 
        if arr[i] != 0: 
            arr[count] = arr[i] 
            count+=1 
    while count < n: 
        arr[count] = 0
        count += 1
arr = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4] 
n = len(arr) 
sorting(arr, n) 
print(arr) 


# In[7]:


list1 = [10, 20, 40, 60, 70,80] 
list2 = [5, 15, 25, 35, 45,60]   
print ("The original list 1 is : " + str(list1)) 
print ("The original list 2 is : " + str(list2))  
size_1 = len(list1) 
size_2 = len(list2)   
res = [] 
i, j = 0, 0  
while i < size_1 and j < size_2: 
    if list1[i] < list2[j]: 
      res.append(list1[i]) 
      i += 1
  
    else: 
      res.append(list2[j]) 
      j += 1
  
res = res + list1[i:] + list2[j:] 
print ("The combined sorted list is : " + str(res))


# In[ ]:




