import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import pandas as pd
import numpy as np
import pickle
import matplotlib.ticker as ticker
from sklearn import preprocessing
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv('updat.csv')


# In[37]:


X=df[['so2','no2','rspm','spm']].values
y=df[['Condition']].values


# In[38]:




# In[39]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.1, random_state=4)
print ('Train set:', X_train.shape, y_train.shape)
print ('Test set:', X_test.shape, y_test.shape)


# In[42]:


from sklearn.neighbors import KNeighborsClassifier
k=3
neigh = KNeighborsClassifier(n_neighbors= k).fit(X_train,y_train)

yhat=neigh.predict(X_test)

pickle.dump(neigh ,open('model.pkl','wb'))

