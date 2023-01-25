# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import math

dfgen = pd.read_csv('gen.csv')   #buildings csv file
dfed = pd.read_csv('edges.csv')  #edges csv file


# In[2]:


temp1 =[]
temp2 = []
datag = []
dtg = []
cnt = 0



for i in dfgen['shape']:
    print(i)
    try:
        temp1.append(i.split(" "))
    except:
        continue
    temp2=[]
    for j in temp1:
        for k in j:
            temp2.append(k.split(","))

    datag.append(temp2)

    
center = []
for building in datag:
    for shape in building:
        center.append([float(shape[0]),float(shape[1])])
    dtg.append(np.mean(center, axis=0))
    print(np.mean(center, axis=0))

# In[25]:


temp1 =[]
temp2 = []
datad = []
dted = []
cnt = 0
for i in dfed['shape']:
    temp1.append(i.split(" "))
    temp2=[]
    for j in temp1:
        for k in j:
            temp2.append(k.split(","))

    datad.append(temp2)


# In[43]:


edge = []
for ed in datad:
    edge.append([float(ed[len(ed)//2][0]) , float(ed[len(ed)//2][1])])


# In[50]:


#nearest edge 1st loop on dataset of the buildings, 2nd loop on ds of the edges
dnn = []

for p in dtg:    
    mind =  (math.dist(p, edge[0]))
    id_ = 0
    for j ,q in enumerate(edge):
        if (mind > (math.dist(p, q))):
            mind = (math.dist(p, q))
            id_ = j
            
    dnn.append(id_)
    


# In[53]:


id_nn = []
for i in dnn:
    id_nn.append(dfed['id'][i])


# In[45]:


dfgen['shape'] = dtg
dfed['shape'] = edge


# In[55]:


dfgen['nearest_edge'] = id_nn


# In[57]:


dfgen.to_csv (r'gen_float.csv', index = False, header=True)
dfed.to_csv (r'edges_float.csv', index = False, header=True)

print("Finish")

# In[ ]:




