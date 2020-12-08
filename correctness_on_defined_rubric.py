#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv from csv 
import reader from csv 
import writer
import pandas as pd

    """
    Purpose: Using a pre-defined list of rubric items to score the summary based on exact matches
    Takes in a csv file that contains student responses in each row and adds a column of scores
    """

rubric = ["can it", "chop it up into sausage", "rub it with soda", "sell it to be eaten on free-lunch counters", 
          "chemistry to change color", "texture and smell", "using strong pickles to get rid of odor", 
          "extract bone and insert hot iron", "stuffing odd and end meats into casing", "mix it with other meat",
          "dosed with borax and glycerin", "change all grade meat to number 1"]

with open('cleaned_jungle_responses.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    
    list_of_scores = [] 
    list_of_rubric_matches = []
    
    # skip the header line in the csv file
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

# add list of scores as a column in csv file
df = pd.read_csv("cleaned_jungle_responses.csv")
print(len(list_of_scores))
print(df.shape)
df['score'] = list_of_scores 

df.to_csv("jungle_scored.csv")

