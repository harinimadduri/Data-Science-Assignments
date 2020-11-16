#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[25]:


#Question 1
data = pd.read_csv('pubg.csv')
data.head()


# In[3]:


#Question 2
data.info()


# In[4]:


#Question 3
data.describe()


# In[5]:


#Question 4
print("The average person kills",data['kills'].mean(),"players.")


# In[6]:


#Question 5
print("99% of people have",np.percentile(data['kills'],99),"kills.")


# In[7]:


#Question 6
print("The most kills ever recorded:",data['kills'].max())


# In[8]:


#Question 7
data.columns


# In[9]:


#Question 8
sns.distplot(data['matchDuration']);

print("Within 1250 to 1500, match duration is high.")


# In[10]:


#Question 9
sns.distplot(data['walkDistance']);


# In[11]:


#Question 10
plt.figure()
plt.subplot(2,1,1)
plt.plot(data['matchDuration'],'-')
plt.subplot(2,1,2)
plt.plot(data['walkDistance'],'-');


# In[12]:


#Question 11
plt.figure(figsize=(10,3))
plt.subplot(1,2,1)
plt.plot(data['matchDuration'],'-')
plt.subplot(1,2,2)
plt.plot(data['walkDistance'],'-');


# In[13]:


#Question 12
sns.pairplot(data.head(700));


# In[14]:


#Question 13
data['matchType'].value_counts()


# In[15]:


#Question 14
sns.barplot(x='matchType',y='killPoints',data=data);
plt.xticks(rotation=70);


# In[16]:


#Question 15
sns.barplot(x='matchType',y='weaponsAcquired',data=data);
plt.xticks(rotation=70);


# In[17]:


#Question 16
data.select_dtypes(['category']).columns


# In[18]:


#Question 17
sns.boxplot(x='matchType',y='winPlacePerc',data=data);
plt.xticks(rotation=70);


# In[19]:


#Question 18
sns.boxplot(x='matchType',y='matchDuration',data=data);
plt.xticks(rotation=70);


# In[20]:


#Question 19
sns.boxplot(x='matchDuration',y='matchType',data=data);
plt.xticks(rotation=70);


# In[21]:


#Question 20
data['KILL'] = data['headshotKills'] + data['teamKills'] + data['roadKills']
data['KILL']


# In[22]:


#Question 21
data['winPlacePerc'] = round(data['winPlacePerc'], 2)
data['winPlacePerc']


# In[23]:


data_arr = []
for i in range(100):
    data_arr.append(data['damageDealt'].sample(50).mean())

sns.distplot(data_arr);
plt.xlabel('damageDealt');


# In[ ]:




