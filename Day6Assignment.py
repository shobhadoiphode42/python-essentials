#!/usr/bin/env python
# coding: utf-8

# In[7]:


list1 = [1,2,3,4,5,6,7,8]
list2 = ["a","b","c","d","e"]

print(dict([(list1[each],list2[each]) for each in range(min(len(list1),len(list2)))]))


# In[ ]:





# In[ ]:




