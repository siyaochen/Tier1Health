#!/usr/bin/env python
# coding: utf-8

# In[6]:


from bokeh.plotting import figure, output_file, show


# In[3]:


import pandas


# In[ ]:





# In[127]:


from bokeh.plotting import figure, output_file, show
import pandas as pd
pd.read_csv("biostats.csv")


# In[129]:


df = pd.read_csv("biostats.csv")


# In[130]:


p=figure(width=500, height=250, x_axis_type="datetime", sizing_mode='stretch_both')


# In[131]:


p.scatter(df["Age"],df["Weight"], color="Blue", alpha=0.5)


# In[132]:


output_file("graph.html")
show(p)


# In[ ]:





# In[ ]:




