#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np
import glob

all_data = pd.DataFrame(columns =['Monday','Tuesday'])
for f in glob.glob("*datasets/weekly_all_data*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe


# In[ ]:




