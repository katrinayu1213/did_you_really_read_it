#!/usr/bin/env python
# coding: utf-8

# In[6]:


# all imports here 
from collections import defaultdict
from gensim import corpora, models
import csv
from pathlib import Path
import pandas as pd
from gensim import similarities
import time

def clean_student_response(response):
    """
    This function cleans student response
    this function is called by query_lsa 
    """
    response = response.replace('"', '' ).replace('“', '' ).replace('”', '' ).replace("'", '' ).replace('\n', ' ').replace('\r', '').lower()
    bad_chars = [';', ':', ".","[","]","#",'!',"?","*", "/", "@", "(", ")", "<", ">", "|", "-", ",", "&", "0", "1", "2", "3","4", "5", "6","7","8","9"]
    for i in bad_chars :
        cleaned_response = response.replace(i, '')
        response = cleaned_response
    print("Cleaned student response: ", cleaned_response)
    return cleaned_response

# Builds corpus with reference text
def build_model_with_ref(corpus_doc_csv): 

    """
    This function cleans corpus documents csv from symbols
    INPUT: corpus doc as csv 
    ATTENTION: assumes that corpus is in csv format; cleaned reference text in given txt file (edit later) 
    tailored for newspaper corpus ie. from 
    this function is called directly 
    """
    
    # add in reference text to first row of corpus  
    with open('ref_text_jungle.txt', 'r') as file:
        ref_text = file.read().replace('\n', '')

    df = pd.read_csv(corpus_doc_csv, engine= 'python')
    new_row = pd.DataFrame({'file_name':'ref_text', 'content': ref_text}, index =[0]) 
    df = pd.concat([new_row, df]).reset_index(drop = True) 

    # clean corpus documents
    documents = df["content"].tolist() 
    bad_chars = [';', ':', ".","[","]","#",'!',"?","*", "/","From", "@", "(", ")", "<", ">", "|", "-", ",", "&", "0", "1", "2", "3","4", "5", "6","7","8","9"]
    
    for document in documents:
#         document.encode('utf-8').strip() # error temporarily addressed 
        for i in bad_chars :
            document = document.replace(i, '')
        
    # remove common words and tokenize
    stoplist = set('for a of the and to in'.split())
    texts = [
        [word for word in document.lower().split() if word not in stoplist]
        for document in documents
    ]

    # remove words that appear only once
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    texts = [
        [token for token in text if frequency[token] > 1]
        for text in texts
    ]

    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
    print("Corpus built and ready for similarity query")
    return (dictionary, lsi, corpus)
    
def query_lsa(response):
    """
    This function cleans queries the lsa model with student response
    INPUT: relies on student response function 
    OUTPUT: lsa_score
    this function is called directly 
    """
    cleaned_response = clean_student_response(response)
    doc = cleaned_response
    
    model = build_model_with_ref("./news_combined_test.csv")
    dictionary = model[0]
    lsi = model[1]
    corpus = model[2]
    
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lsi = lsi[vec_bow]  # convert the query to LSI space

    index = similarities.Similarity('workdir/',lsi[corpus],num_features=2)  # transform corpus to LSI space and index it

    sims = index[vec_lsi]  # perform a similarity query against the corpus

    score_query = list(enumerate(sims))
    tuple = score_query[0]
    lsa_score = tuple[1]
    print("LSA Score: ", lsa_score)
    return lsa_score

query_lsa("sample student response, here!1")


# In[ ]:




