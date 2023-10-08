#!/usr/bin/env python
# coding: utf-8

# # Euro exchange currency
# 
# ### Websites
# 
# ###### Twilio: 
# https://www.twilio.com/en-us
# 
# ###### Weather API: 
# https://exchangeratesapi.io/

# ### Twilio tokens:
# ###### Account SID:
# AC33ae0ed26f623a42d5767445994807cf

# In[1]:


account_sid= "AC33ae0ed26f623a42d5767445994807cf"


# ###### Auth Token:
# c33ae12852e70b97e3078b68fc8de318

# In[2]:


auth_token = "c33ae12852e70b97e3078b68fc8de318"


# ###### Twilio Phone Number:
# +12138141175

# In[4]:


phone_number = "+12138141175" 


# ## Exchange rate API

# ###### API KEY
# e3c05093f41dd1ee2c80675720b518c9

# In[5]:


api_key = "e3c05093f41dd1ee2c80675720b518c9"


# ## Install Libraries

# ###### Request:
# conda install -c anaconda requests
# 
# ###### Twilio:
# conda install -c conda-forge twilio

# ### Import Libraries

# In[6]:


from twilio.rest import Client
import requests
import requests.exceptions
import json
import pandas as pd
import datetime


# ### URL

# ###### Documentation
# https://exchangeratesapi.io/documentation/

# In[8]:


url = "http://api.exchangeratesapi.io/v1/latest?access_key="+api_key


# In[9]:


url


# ### Request

# In[10]:


response= requests.get(url).json()


# ###### NOTE:
# Print the response in order to look for the information we need

# In[13]:


response


# In[12]:


response.keys()


# ###### NOTE:
# We'll use the 'rates' key

# In[14]:


response['rates']


# ###### NOTE:
# We will look for the currency of which we want to know its equivalence

# In[18]:


response['rates']['MXN']


# In[20]:


response['rates']['USD']


# In[21]:


dollar_peso= response['rates']['MXN']/ response['rates']['USD']


# In[22]:


dollar_peso


# ###### DATE

# In[42]:


response['date']


# In[43]:


response['date'].split("-")


# In[49]:


year = response['date'].split("-")[0]


# In[50]:


year


# In[56]:


month = response['date'].split("-")[1]


# In[57]:


month


# In[58]:


day=response['date'].split("-")[2]


# In[59]:


day


# In[60]:


list_date=[day,month,year]


# In[61]:


list_date


# In[62]:


real_date="-".join(list_date)


# In[63]:


real_date


# ### Dataframe

# In[67]:


date = str(real_date)
euro = str(1)
peso = str(response['rates']['MXN'])
dollar = str(dollar_peso)


#  ### Message template

# In[70]:


message_template = "Hello, today " + date + " the value of the euro is " + peso + " and the value of the dollar is " + dollar


# ### Message

# In[71]:


client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body= message_template,
         from_= phone_number,
         to='+524181709157'
     )

print('Message sent' + message.sid)

