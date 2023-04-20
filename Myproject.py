#!/usr/bin/env python
# coding: utf-8

# In[77]:


import numpy as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[78]:


df=pd.read_csv("amazon_data_set.csv")
df.head(5)


# In[79]:


df.shape


# In[80]:


df.duplicated().value_counts()


# In[81]:


dfx=df.copy()


# In[82]:


dfx.dtypes


# In[83]:


dfx.isna().sum()


# In[84]:


dfx[dfx["rating_count"].isna()]


# In[85]:


dfx=dfx.dropna()


# In[86]:


dfx.isna().sum()


# In[87]:


dfx["rating_count"]=dfx["rating_count"].str.replace(",","")
dfx["discounted_price"]=dfx["discounted_price"].str.replace("₹","").str.replace(".","").str.replace(",","")
dfx["discount_percentage"]=dfx["discount_percentage"].str.rstrip("%")
dfx["discounted_price"]=dfx["discounted_price"].astype(float)
dfx["actual_price"]=dfx["actual_price"].str.replace("₹","").str.replace(",","")
dfx["actual_price"]=dfx["actual_price"].str.replace(".","")
dfx["actual_price"]=dfx["actual_price"].astype(int)
dfx["discount_percentage"]=dfx["discount_percentage"].astype(float)


# In[88]:


dfx["discount_percentage"]=dfx["discount_percentage"]/100


# In[89]:


dfx.head(5)


# In[90]:


dfx["rating_count"]=dfx["rating_count"].astype(int)


# In[91]:


dfx[["rating"]].value_counts()


# In[92]:


dfx["rating"]=dfx["rating"].str.replace("|","4")


# In[93]:


dfx["rating"].astype(float)


# In[94]:


dfx.dtypes


# In[95]:


dfx.head()


# In[96]:


df2=dfx["category"].str.split("|",expand=True)
df2


# In[97]:


df2 = df2.rename(columns={0:'category_1', 2:'category_3'})


# In[102]:


dfx["Major_category"]=df2["category_1"]

dfx["Sub_category"]=df2["category_3"]


# In[99]:


dfx.drop(columns="category",inplace=True)


# In[100]:


dfx=dfx.drop(columns={"img_link","product_link"},inplace=True)


# In[101]:


dfx["product_id"]=dfx["product_id"].str.strip()


# In[ ]:


dfx["rating"]=dfx["rating"].astype(float)


# In[ ]:


dfx.dtypes


# In[ ]:


dfx['Score'] = pd.cut(x=dfx['rating'], bins=[1, 3, 4, 5],
                     labels=['Low', 'Medium', 'High'])


# In[ ]:


dfx[["rating","Score"]].value_counts()


# In[ ]:


dfx


# In[ ]:


df3=dfx["user_id"].str.split(",",expand=False)
df3=df3.explode()
df3=df3.reset_index(drop=True)


# In[ ]:


df4=dfx["user_name"].str.split(",",expand=False)
df4=df4.explode()
df4=df4.reset_index(drop=True)


# In[ ]:


df5=pd.DataFrame(df3)
df5=df5.reset_index(drop=True)


# In[ ]:


df6=pd.DataFrame(df4)
df6=df6.reset_index(drop=True)


# In[ ]:


df7= pd.merge(df5, df6, left_index=True, right_index=True)
df7


# In[ ]:





# In[ ]:




