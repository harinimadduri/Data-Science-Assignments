#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Question 1
import numpy as num
array = num.arange(2,51,3)
print(array)


# In[5]:


#Question 2
import numpy as num
listone = []
listtwo = []
for i in range(5):
    input1 = int(input())
    listone.append(input1)
print("List one :",listone)
for i in range(5):
    input1 = int(input())
    listtwo.append(input1)
print("List Two", listtwo)
# conversion of List to Array
arrayone = num.array(listone)
arraytwo = num.array(listtwo)
print("List to array convert 1 :", arrayone)
print("List to array convert 2 :", arraytwo)
# concatenation of arrays
arrayconcat = num.concatenate((arrayone, arraytwo))
print("concatenation of arrays are :", arrayconcat)
# Sorting of array
print("Sorted array :", num.sort(arrayconcat))


# In[7]:


#Question 3
import numpy as num

arrayone = num.array([[2, 4, 8], [4, 8, 2], [5, 3, 1]])
print("calculate Dimensions of array is :", arrayone.ndim)

print("Size of an array is :", arrayone.size)


# In[9]:


#Question 4
import numpy as num
array = num.arange(int(input()))
print("Shape of 1D :", array.shape)
twodarrayrow = array[num.newaxis]
print("Row of 2D :", twodarrayrow.shape)
twodarraycol = array[:, num.newaxis]
print("Column of 2D :", twodarraycol.shape)


# In[11]:


#Question 5
import numpy as num
arrayone = num.square([2,5,7,6,4,8,3,9,11,2,1,5,2])  # square of numpy array
arraytwo = num.square([5,4,6,9,3,2,1])  # square of numpy array
print(" horizontal stack :", num.hstack((arrayone, arraytwo)))
print("vertical stack : ", np.hstack((arrayone, arraytwo)))


# In[14]:


#Question 6
import numpy as num
ar= num.array([4,5,6,7,8,9,0,1])
unique,counts = num.unique(ar, return_counts=True)
ar = num.asarray((unique, counts)).T
print(ar)


# In[ ]:




