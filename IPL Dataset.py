#!/usr/bin/env python
# coding: utf-8

# import pandas as pd
# from matplotlib import pyplot as plt

# In[3]:


#loading ipl matches dataset
ipl=pd.read_csv('matches.csv')


# In[4]:


ipl.head()


# In[5]:


ipl.shape


# In[6]:


#Getting frequency of most man of the match awards
ipl['player_of_match'].value_counts()


# In[8]:


#Getting top 10 of most man of the match awards
ipl['player_of_match'].value_counts()[0:10]


# In[12]:


#Bar plot for top five most man of the match awards
list(ipl['player_of_match'].value_counts()[0:5].keys())


# In[23]:


plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]),color='g')
plt.show()


# In[26]:


#Getting the frequency of result coloumn
ipl['result'].value_counts()


# In[31]:


#finding out the number of toss wins w.r.t each 
ipl['toss_winner'].value_counts()


# In[34]:


#extracting the records where a team won batting first
batting_first=ipl[ipl['win_by_runs']!=0]


# In[37]:


batting_first.head()


# In[38]:


#Number of wins w.r.t each team after batting first
batting_first['winner'].value_counts()


# In[51]:


#making a bar-plot for top 3 teams with most wins after batting first
plt.figure(figsize=(6,6))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=["blue","yellow","orange"])
plt.show()


# In[58]:


#making a pie chart
plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[59]:


#extracting number of wins w.r.t each team after batting second
batting_second=ipl[ipl['win_by_wickets']!=0]


# In[63]:


batting_second['winner'].value_counts()


# In[67]:


#making a histogram for frequency of wins w.r.t number of wickets
plt.figure(figsize=(5,5))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.show()


# In[69]:


plt.figure(figsize=(5,5))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[72]:


#Looking at number of matches played each season
ipl['season'].value_counts()


# In[73]:


#Most number of matches played in a city
ipl['city'].value_counts()


# In[74]:


#Finding out how many times team has won match after winning toss
import numpy as np
np.sum(ipl['toss_winner']==ipl['winner'])


# In[76]:


325/636


# In[77]:


deliveries=pd.read_csv('deliveries.csv')


# In[78]:


deliveries.head()


# In[83]:


deliveries['match_id'].unique()


# In[ ]:





# In[ ]:




