#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# EDA Using Pyhon - Project Name -"Ed Tech Business Intelligence"


# In[ ]:


#Importing  all Libraries required for analysis


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Importing Dataset - as the given file is csv
df=pd.read_csv(r"C:\Users\HP\Downloads\online_All_Business_p1_p626.csv")


# In[3]:


df.head() #Getting Top 5 Rows of given dataset


# In[4]:


df.tail() #Getting Bottom 5 Rows


# In[5]:


df.info()


# In[6]:


df.isnull().sum() #getting null value sum


# In[7]:


#As we see above discount_price__amount,discount_price__currency,discount_price__price_string  are having null values and 
# in further analysis I will handle the null values


# In[8]:


df.drop(['discount_price__price_string','price_detail__price_string','discount_price__currency','published_time','avg_rating_recent'],
        axis=1,inplace=True) #Dropping the some columns which are having same data and not required for further analysis.


# In[9]:


df.describe()


# In[30]:


df.head(1)


# In[11]:


df.isnull().sum()


# In[10]:


#As we in in df.describe() for column name "discount_price__amount" most of the dataset value lying around 455 amount so we will
#replace null values with 455
df["discount_price__amount"].fillna(455,inplace=True)


# In[11]:


df.isnull().sum()


# In[12]:


df.head(1)


# In[16]:


#Plotting the graph to get idea about how many courses are paid and unpaid.
plt.figure(figsize=(5,5))
sns.countplot(x=df['is_paid'])
plt.title('Published lectures to prices')


# In[17]:


#As we see in above graph is showing value for TRUE that maens - All Courses in this dataset is paid courses


# In[13]:


n=len(pd.unique(df['id']))
n #Getting Total numbers of unique id count


# In[14]:


#Regression Plot Analysis for Num-Published_lectures Vs Price_detail_Amount
plt.figure(figsize=(10,5))
sns.regplot(y=df['num_published_lectures'],x=df['price_detail__amount'])
plt.title('Published lectures to prices')


# In[ ]:


#There is little correaltion between this as num_published_lectures is increasing price amount is also increasing.


# In[38]:


plt.figure(figsize=(10,5))
sns.scatterplot(y=df['num_published_practice_tests'],x=df['price_detail__amount'])
plt.title('Published practice tests to prices')


# In[ ]:


#As we see in above scatterplot there is no any particular trend found between num_published_practice tests 
#and price deatil amount


# In[16]:


plt.figure(figsize=(10,5))
sns.scatterplot(y=df['num_reviews'],x=df['rating'])
plt.title('reviews to rating')


# In[17]:


#As we see in above scatterplot we get the conclusion that data is gathered around where the course rating is in between 
#4.0 to 5.0 that means higher the rating will ultimately aim to higher for number of reviews


# In[42]:


#Top 10 courses by rating
top_rated=df[['title','rating']].sort_values(by='rating',ascending=False).head(10)
top_rated


# In[43]:


#Top 10 courses by num_published_practice_testes
df[['title','num_published_practice_tests','rating']].sort_values(by='num_published_practice_tests',ascending=False).head(10)


# In[18]:


#Top 10 courses by num_published_lectures
df[['title','num_published_lectures','rating']].sort_values(by='num_published_lectures',ascending=False).head(10)


# In[ ]:


#As we see above the course name "Accounting–Financial Accounting Total-Beginner..." have the maximum num_published_lectures.


# In[19]:


#Top 10 courses by price_detial_amount - most costliest courses
df[['title','price_detail__amount','discount_price__amount','rating']].sort_values(by='price_detail__amount',ascending=False).head(10)


# In[20]:


#Top 10 courses by price_detial_amount - most cheapiest courses
df[['title','price_detail__amount','discount_price__amount','rating']].sort_values(by='price_detail__amount',ascending=True).head(10)


# In[ ]:


#As we see in above analysis based on price deatil amount & price discount amount the maximum amount for most of courses 
#is 12800Rs and with having same discount price amount and the minimum amount for most of courses is 1280 Rs and 
#with having same discount price amount


# In[21]:


df.created


# In[22]:


type(df['created'])


# In[25]:


#converting created column to datetime
df['created']=pd.to_datetime(df['created'])


# In[27]:


df['date_created']=df['created'].dt.date #extracting date part from created column and giving name as "date_created"
df.date_created


# In[30]:


df['year']=pd.DatetimeIndex(df.date_created).year
df['month']=pd.DatetimeIndex(df.date_created).month
df['day']=pd.DatetimeIndex(df.date_created).day


# In[31]:


#Plot of Num_courses_Created Vs Count of Courses
plt.figure(figsize=(10,5))
sns.countplot(x=df['year'],order=df.year.value_counts().sort_values(ascending=False).index)
plt.title('num_courses_per_year')


# In[ ]:


#Most of the courses created in year 2018


# In[33]:


#Saving this EDA file of datset to CSV
df.to_csv(r"C:\Users\HP\Downloads\edtechanlysis.csv")

