#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install selenium')


# In[3]:


get_ipython().system('pip install webdriver_manager')


# In[10]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[30]:


#define opotions and set browser capabilities
options=webdriver.ChromeOptions()
#options.add_argument('--some-option')


# In[31]:


#Create Webdriver instance with options
driver=webdriver.Chrome(options=options)


# In[32]:


#Navigate to a website
driver.get('https://www.myntra.com/')


# In[33]:


search=driver.find_element(By.XPATH,".//input[@class='desktop-searchBar']")


# In[34]:


search.send_keys("shirts for men")


# In[35]:


search.send_keys(Keys.ENTER)


# In[42]:


brand=driver.find_elements(By.XPATH,".//h3[@class='product-brand']")
print(brand)


# In[43]:


price=driver.find_elements(By.XPATH,".//span[@class='product-discountedPrice']")
print(price)


# In[45]:


prod=driver.find_elements(By.XPATH,".//h4[@class='product-product']")
print(prod)


# In[47]:


df['brand']=brand
df['prod']=prod
df['price']=price


# In[ ]:




