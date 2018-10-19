
# coding: utf-8

# # Change in movie genre development trends since 1970
# ### Analysis based on IMDB data set.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Reading the main file

# In[2]:


data_set = pd.read_csv('IMDB data.tsv', sep='\t',low_memory=False)
data_set.head(5)


# Filtering the data to only contain movie type

# In[3]:


movies= data_set[data_set.loc[:,'titleType']=='movie']
movies.head()


# Filtering out the extra columns to have the genre and release date only

# In[4]:


genre_yr = movies.loc[:,['startYear','genres']]
genre_yr.head()


# Checking if there are rows with missing data

# In[5]:


genre_yr.isnull().any()


# Finding the total types of genres avaible

# In[6]:


temp = genre_yr['genres'].str.split(',',expand = True)
all_genres = pd.unique(temp[:].values.ravel('K'))
all_genres


# Deleting rows with genre '\\N' and None

# In[7]:


temp = genre_yr[genre_yr.loc[:,'genres']=='\\N']
genre_yr = genre_yr.drop(temp.index)
temp = genre_yr[genre_yr.loc[:,'genres']==None]
genre_yr = genre_yr.drop(temp.index)


# Checking the total genres again

# In[8]:


temp = genre_yr['genres'].str.split(',',expand = True)
all_genres = pd.unique(temp[:].values.ravel('K'))
all_genres


# Counting the total number of movies by year in each genre

# In[9]:


TMG = pd.DataFrame() #Total Movie Genre by year
for i in range(28):
    temp = genre_yr[genre_yr['genres'].str.contains(all_genres[i])]
    
    TMG[all_genres[i]] = temp.groupby(['startYear']).genres.count()


# Checking the value of TMG

# In[10]:


TMG.head()


# Filtering out movies before 1970

# In[11]:


TMG = TMG.drop(TMG.index[:64])
TMG.head()


# In[12]:


TMG.tail()


# Filtering out upcoming movie dates, i.e. 2018 onwards

# In[13]:


TMG = TMG.drop(TMG.index[-4:])
TMG.tail()


# Plotting the graph of a movie genres over years}

# In[14]:


plt.figure(figsize=(15,10))
plt.plot(TMG)

plt.xticks(np.arange(0,75, step =7))
plt.legend(all_genres)
plt.yscale(value= 'linear')
plt.ylabel('Number of movies produced', rotation = 'vertical', size = 18)
plt.xlabel('Years', size = 18)
plt.grid(True)
plt.show()


# ### Comparing the number of films per genre in 2000 vs 2017

# In[15]:


plt.figure(figsize=(15,5))
plt.bar(['Romance', 'Documentary', 'Biography', 'Drama', 'Adventure',
       'Comedy', 'Crime', 'War', 'Sci-Fi', 'History', 'Western',
       'Fantasy', 'Action', 'Horror', 'Thriller', 'Mystery', 'Animation',
       'Music', 'Musical', 'Sport', 'Family', 'Film-Noir', 'Adult',
       'News', 'Game-Show', 'Reality-TV', 'Talk-Show', 'Short'],height = TMG.iloc[30,:])
plt.xticks(fontsize=10,rotation='vertical')
plt.ylabel('Number of movies produced', rotation = 'vertical', size = 18)
plt.xlabel('Year: 2000', size = 18)
plt.show()


# In[16]:



plt.figure(figsize=(15,5))
plt.bar(['Romance', 'Documentary', 'Biography', 'Drama', 'Adventure',
       'Comedy', 'Crime', 'War', 'Sci-Fi', 'History', 'Western',
       'Fantasy', 'Action', 'Horror', 'Thriller', 'Mystery', 'Animation',
       'Music', 'Musical', 'Sport', 'Family', 'Film-Noir', 'Adult',
       'News', 'Game-Show', 'Reality-TV', 'Talk-Show', 'Short'],height = TMG.iloc[-1,:])
plt.ylabel('Number of movies produced', rotation = 'vertical', size = 18)
plt.xlabel('Year: 2017', size = 18)

plt.xticks(fontsize=10,rotation='vertical')

plt.show()


# Combining the Two bar graphs for a better understanding.

# In[17]:


labels = ['Romance', 'Documentary', 'Biography', 'Drama', 'Adventure',
       'Comedy', 'Crime', 'War', 'Sci-Fi', 'History', 'Western',
       'Fantasy', 'Action', 'Horror', 'Thriller', 'Mystery', 'Animation',
       'Music', 'Musical', 'Sport', 'Family', 'Film-Noir', 'Adult',
       'News', 'Game-Show', 'Reality-TV', 'Talk-Show', 'Short']
y2000 = TMG.iloc[30,:]
ind = np.arange(28)
width = 0.4

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, y2000, width, color='royalblue')


y2017 = TMG.iloc[-1,:]
rects2 = ax.bar(ind+width, y2017, width, color='seagreen')

fig.set_size_inches(15, 10)
fig.savefig('test2png.png', dpi=200)

ax.set_ylabel('Number of movies produced', rotation = 'vertical', size = 18)
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(labels, rotation='vertical')

ax.legend((rects1[0], rects2[0]), ('Year: 2000', 'Year: 2017'))

plt.show()


# Deleting outliers

# In[18]:


del TMG['Documentary']
del TMG['Drama']


# In[19]:


plt.figure(figsize=(15,10))
plt.plot(TMG)

plt.xticks(np.arange(0,75, step =7))
plt.legend(['Romance','Biography', 'Adventure',
       'Comedy', 'Crime', 'War', 'Sci-Fi', 'History', 'Western',
       'Fantasy', 'Action', 'Horror', 'Thriller', 'Mystery', 'Animation',
       'Music', 'Musical', 'Sport', 'Family', 'Film-Noir', 'Adult',
       'News', 'Game-Show', 'Reality-TV', 'Talk-Show', 'Short'])
plt.ylabel('Number of movies produced', rotation = 'vertical', size = 18)
plt.xlabel('Years', size = 18)
plt.grid(True)
plt.show


# ## Plotting the well known genres.

# In[20]:


plt.figure(figsize=(15,10))
plt.plot(TMG.loc[:,['Romance','Sci-Fi','Action','History']])

plt.xticks(np.arange(0,47, step =4))
plt.legend(['Romance','Sci-Fi','Action','History'])
plt.grid(True)
plt.ylabel('Number of movies produced', rotation = 'vertical', size = 18)
plt.xlabel('Years', size = 18)
plt.show

