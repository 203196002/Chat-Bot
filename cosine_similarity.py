#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:13:34 2020

@author: saurabhadhikary
"""
import re
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
sw = stopwords.words('english')
from data_cleaner import pre_process
import pandas as pd
import os
import matplotlib as plt

def cos_get(data, user_ques):
    total = []
    l1 = []
    l2 = []
    ques = word_tokenize(pre_process(data))
    total = user_ques + ques

    for w in total: 
        if w in user_ques: l1.append(1) # create a vector 
        else: l1.append(0) 
        if w in ques: l2.append(1) 
        else: l2.append(0)        
    cs = cosine_similarity((l1,l2))
    print("cs -",cs[0][1])
    return cs[0][1] # return a matrix

def get_similar_questions(user_ques,q_class):
    q_class = str(q_class).lower().strip()
    df = pd.read_csv('data/complete_df.csv')
    df = df[df.keyword.str.contains(str(q_class),na=False,regex=True)]
    user_ques = word_tokenize(pre_process(user_ques))
    user_ques =[w for w in user_ques if not w in sw]
    df['cos_sim'] = df['parsed_title'].apply(lambda x:cos_get(x,user_ques) )
    df = df.sort_values('cos_sim',ascending=False)
    df = df.query('cos_sim>0.7')
    output = df[:1]
    if len(output):
        return output['parsed_body_ans'].values[0]
    else:
        return None

# train_df = pd.read_csv('data/train.csv')
# print("done")
score_df = pd.read_csv('score.csv')

#column_names = ["cos_tr", "cos_te", "c"]

# score_df = pd.DataFrame(columns = column_names)
# user_ques = 'how to plot a graph'
# user_ques = word_tokenize(pre_process(user_ques))
# user_ques =[w for w in user_ques if not w in sw]
# score_df['cos_te'] = test_df['parsed_title'].apply(
#      lambda x:get_similar_questions(x,'Python') )
# score_df['parsed_body_ans'] = train_df['parsed_body_ans']
# score_df.to_csv('score.csv')
score_df['sim'] = cos_get(score_df['cos_te'],score_df['parsed_body_ans'])
score_df.reset_index().plot(x ='index', y='sim', kind = 'scatter')
#monthly_mean.reset_index().plot(x='index', y='A')
print("complete")
plt.show()
#print("similarity :\n\n\n",get_similar_questions('color of plot','Python'))