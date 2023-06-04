
# coding: utf-8

# In[4]:


import seaborn as sns ### For plotting 
import matplotlib.pyplot as plt ### for showing plots

tips_data = sns.load_dataset("tips")


# In[5]:


tips_data.head()


# In[6]:


tips_data.describe()###Describing the dataset 


# In[17]:


###Plot histogram
sns.distplot(tips_data["total_bill"], kde=False).set_title ("History of Total Bills")
plt.show()


# In[20]:


###Plot histogram
sns.distplot(tips_data["tip"], kde=False).set_title ("History of Tip")
plt.show()


# In[23]:


sns.distplot(tips_data["tip"], kde=False)
sns.distplot(tips_data["total_bill"], kde=False).set_title ("History of Total Bills & Tip")

plt.show()


# In[24]:


sns.boxplot(tips_data["total_bill"]).set_title("Box Plot of Total Bill")
plt.show()


# In[25]:


sns.boxplot(tips_data["tip"]).set_title("Box Plot of Tip")
plt.show()


# In[26]:


sns.boxplot(tips_data["tip"])
sns.boxplot(tips_data["total_bill"]).set_title("Box Plot of Total Bill & Tip")


# In[29]:


sns.boxplot(x = tips_data["tip"], y= tips_data["smoker"])
g = sns.FacetGrid(tips_data, row = "smoker")
g = g.map(plt.hist,"tip")

plt.show()


# In[31]:


sns.boxplot(x = tips_data["tip"], y= tips_data["time"])

g = sns.FacetGrid(tips_data, row = "time")
g = g.map(plt.hist,"tip")
plt.show()


# In[34]:


sns.boxplot(x = tips_data["tip"], y= tips_data["day"]).set_title("Boxplot of tips by data of the week")
g = sns.FacetGrid(tips_data, row = "day")
g = g.map(plt.hist, "tip")
plt.show()

