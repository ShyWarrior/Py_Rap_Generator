#!/usr/bin/env python
# coding: utf-8

# In[5]:


data_file="Rap/lyrics1.txt"


# In[6]:


def load_file(file_name):
    f=open(file_name, "r")
    content=f.read()
    f.close
    return content


# In[7]:


load_file(data_file)


# In[8]:


training_data="Hello Hello World World"


# In[9]:


def createTable(text, k=3):
    T={}
    for i in range(len(text)-k):
        X=text[i:i+k]
        y=text[i+k]
        if X in T:
            if y in T[X]:
                T[X][y] +=1
            else:
                T[X][y]=1
        else:
            T[X]={
                y: 1
            }
    return T
        


# In[10]:


createTable(training_data)


# In[11]:


def probTable(T):
    for key in T:
        total=sum(T[key].values())
        for ikey in T[key]:
            T[key][ikey]=T[key][ikey]/total
    return T


# In[12]:


createTable(training_data)


# In[13]:


probTable(_)


# In[14]:


import numpy as np


# In[15]:


model=probTable(createTable(training_data))


# In[16]:


def sampleNext(ctx,inp):
    inp=inp[-3:]
    if inp in ctx:
      # return max(ctx[inp].items(),key=lambda x: x[1])[0]
      probable_chars=list(ctx[inp].keys())
      freq=list(ctx[inp].values())
      return np.random.choice(probable_chars,p=freq)
    else:
        return " " 
        


# In[17]:


sampleNext(model, "Hell")


# In[18]:


model=probTable(createTable(load_file(data_file)))


# In[19]:


sampleNext(model,"mohabba")


# In[20]:


def genText(ctx,inp,length=1000):
    text=inp
    for _ in range(length):
        text+=sampleNext(ctx,text[-3:])
    return text


# In[21]:


print(genText(model, "bad boys"))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




