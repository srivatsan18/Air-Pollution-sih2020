#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
df=pd.read_csv('upedit.csv')
df.head()
X=df[['Number','year']]
Y=df['AQI']
from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=10,random_state=0)
regressor.fit(X,Y)
#print(regressor.predict([[1,2012]]))


# In[2]:


import pickle
pickle.dump(regressor,open('RandomReg.pkl','wb'))


# In[ ]:
