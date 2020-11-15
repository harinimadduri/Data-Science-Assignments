#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Question 1
import pandas as p
print(p.__version__)


# In[13]:


#Question 2
import numpy as n
import pandas as p
data=n.array([1,2,3,5,6,9,8,3])
print(data)
print(p.Series(data))


# In[12]:


#Question 3
import pandas as p
data = p.Series([1,2,3,5,6,9,8,3])
print("Series is :", data)

print("index of above column :", data.to_frame().reset_index())


# In[16]:


#Question 4
import seaborn as s
import pandas as p
print("All list present in the seaborn library :", s.get_dataset_names()) # list of all dataset in the seaborn
print()
mpg = s.load_dataset('mpg')
print("mpg data set from seaborn :", mpg) # loading mpg data set from seaborn library
print()
print("'anagrams' data set from seaborn :", s.load_dataset('anagrams'))
print()
print("car_crashes data set from seaborn :", s.load_dataset('car_crashes'))
print()
print(p.read_csv("student_records.csv")) 


# In[18]:


#Question 5
import seaborn as s
import pandas as p
dataset = s.load_dataset('mpg')
print(dataset)
df = p.DataFrame(dataset)
print(" country origin :", df.origin.unique())


# In[19]:


#Question 6
import seaborn as s
import pandas as p
dataset = s.load_dataset('mpg')
print(dataset)
df = p.DataFrame(dataset)
print(" Data set extracted only for usa :", df[df['origin'].str.contains("usa")])


# In[ ]:




