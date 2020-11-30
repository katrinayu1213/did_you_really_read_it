#!/usr/bin/env python
# coding: utf-8

# In[90]:


import csv
from csv import reader
from csv import writer


# In[91]:


# create a list of scores for each text

rubric = ["can it", "chop it up into sausage", "rub it with soda", "sell it to be eaten on free-lunch counters", 
          "chemistry to change color", "texture and smell", "using strong pickles to get rid of odor", 
          "extract bone and insert hot iron", "stuffing odd and end meats into casing", "mix it with other meat",
          "dosed with borax and glycerin", "change all grade meat to number 1"]

with open('cleaned_jungle_responses.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    
    # score each text 
    list_of_scores = [] 
    list_of_rubric_matches = []
    
    # skip the header line
    next(read_obj)
    for row in csv_reader:
        # clean the text: quotes, lower case
        row[0] = row[0].replace('"', '' ).replace('“', '' ).replace('”', '' ).replace("'", '' ).replace('\n', ' ').replace('\r', '').lower()

        score = 0
        rubric_matched = []
        
        # see if it matches any rubric items
        for item in rubric:
            if item in row[0]:
                rubric_matched.append(item)
                score += 1
                pass
        list_of_scores.append(score)
        list_of_rubric_matches.append(rubric_matched)
#     print(list_of_scores)
#     print(len(list_of_scores))


# In[93]:


# add list of scores as a column in csv file
import pandas as pd
df = pd.read_csv("cleaned_jungle_responses.csv")
print(len(list_of_scores))
print(df.shape)
df['score'] = list_of_scores 

df.to_csv("jungle_scored.csv")


# In[ ]:




