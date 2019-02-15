#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:28:29 2019

@author: rushikesh

"""
import pandas as pd
import numpy as np
user_history = pd.read_pickle('User_Prod_Label.pkl')
descriptions = pd.read_pickle('descriptions.pkl')

from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer().fit(descriptions[0])
len(vect.get_feature_names())


ind = 0
curr_user_prods = np.array(user_history[0])
current_user_bought = np.where(curr_user_prods==1)[0]

user_description = ' '.join(str(descriptions[0][i]) for i in current_user_bought)

user_vector = vect.transform([user_description])

product_vector = vect.transform(descriptions[0])


#predicting products based on previously bought products
from sklearn.neighbors import NearestNeighbors

#Since the tf-idf already normalizes the vector we can use euclidean distance also
classifier = NearestNeighbors(n_neighbors=5)
classifier.fit(product_vector)
ans = classifier.kneighbors(user_vector, n_neighbors=10)
ind = ans[1][0]


#Generating all users embeddings
user_descriptions = []
for i in range(20):
    curr_user = np.array(user_history[i:i+1])
    print(curr_user)
    current_user_bought = np.where(curr_user[0]==1)[0]
    print(current_user_bought)
    curr_user_description = ' '.join(str(descriptions[0][i]) for i in current_user_bought)
    #user_vector = vect.transform([user_description])
    user_descriptions.append(curr_user_description)

user_embeddings = vect.transform(user_descriptions)

#Finding similar users based on purchase interests
test_user = user_embeddings[0]
user_classifier = NearestNeighbors(n_neighbors=10)
user_classifier.fit(user_embeddings)
user_ans = user_classifier.kneighbors(test_user, n_neighbors=10)
user_ind = user_ans[1][0]

#Concatenate history of top k similar users
def Union(lst1, lst2): 
    final_list = list(set(lst1) | set(lst2)) 
    return final_list 

con_user_history = [] #product indices
count=0
k=3
for i in user_ind:
    curr_user = np.array(user_history[i:i+1])
    print(curr_user)
    current_user_bought = np.where(curr_user[0]==1)[0]
    print(current_user_bought)
    con_user_history = Union(con_user_history, current_user_bought)
    count+=1
    if count==k:
        break
    
concat_description=""   
for c in con_user_history:
    concat_description += "".join(descriptions[0][c])
    
concat_vect = vect.transform([concat_description])
collab_classifier = NearestNeighbors(n_neighbors=10)
collab_classifier.fit(product_vector)
collab_ans = collab_classifier.kneighbors(concat_vect, n_neighbors=10)
collab_ind = ans[1][0]