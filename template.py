#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Use magic commands (%)

# When modifying libraries, no need to restart the kernel
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import src.copa.util_functions as u


# In[5]:


u.setPandasOptions()

