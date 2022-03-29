#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd


# In[24]:


data=pd.read_csv(r"C:\Users\krishna\Downloads\1. Weather Data.csv")
print(data)


# In[25]:


data.shape


# In[26]:


data.info


# In[27]:


data.value_counts()                                            


# In[28]:


data.dtypes


# In[29]:


data['Visibility_km'].unique()


# In[30]:


data['Weather'].value_counts()


# In[ ]:





# In[31]:


data['Weather'].nunique


# In[28]:


data.Weather=='Clear'
print(data.Weather)
data[data.Weather=='Clear']


# In[ ]:





# In[32]:


data.groupby('Weather').get_group('Clear')


# when the wind speed was '7'

# In[33]:


data['Wind Speed_km/h']==7
data[data['Wind Speed_km/h']==7]


# In[34]:


data['Wind Speed_km/h']==7


# In[35]:


data.Visibility_km.mean()


# mean visibility

# standered deviation
# 

# In[36]:


data.Visibility_km.std()


# varience of relative humidity

# In[37]:


data['Rel Hum_%'].var()


# In[38]:


#str contains 
data[data['Weather'].str.contains('Snow')].head(10)
data[data['Weather'].str.contains('Snow')].tail(10)


# when wind speed is below 20 and Visibility_km is greater than 35

# In[39]:


data[(data['Wind Speed_km/h']<5) & (data['Visibility_km']>35)]


# mean value groupwise for weather conditions->
# 

# In[40]:


data.groupby('Weather').mean()


# when weather condition is clear rel hum more than 30 % or visibility is less than 5km

# In[41]:


data[(data['Weather']=='Clear') & (data['Rel Hum_%']>30) | (data['Visibility_km']<5)]


# In[ ]:





# In[ ]:




