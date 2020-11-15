#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Question 1
x=[]
for i in range(10):
    y=int(input())
    if y%2==0:x.append(y)
print(x)


# In[2]:


#Question 2
x=[i for i in range(1,10+1) if i%2==0]
print(x)


# In[3]:


#Question 3
y={}
for i in range(1,int(input())+1):y[i]=i*i
print(y)


# In[7]:


#Question 4
import math
(x,y)=(0,0)
for i in range(int(input())):
    a,b=input().split()
    a,b=str(a),int(b)
    if a=="DOWN":x,y=x,y-b
    elif a=="LEFT":x,y=x-b,y
    elif a=="RIGHT":x,y=x+b,y
    else:x,y=x,y+b
print(round(math.sqrt((x**2)+(y**2))))


# In[ ]:




