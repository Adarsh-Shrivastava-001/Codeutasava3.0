#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:20:38 2019

@author: adarsh
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

user_data=pd.read_csv('user.csv')
prod_data=pd.read_csv('prod.csv')

labels=pd.read_csv('labels.csv')

user_mat=np.array(user_data)     
prod_mat=np.array(prod_data)

user_mat=np.random.random((20,10))
prod_mat=np.random.random((20,10))

labels=np.random.choice(2, 400, p=[0.7,0.3]).reshape(20,20)

epochs=1000
eta=0.05
lam=0.01

def sigmoid(arr):
    return 1/(1+np.exp(-1*arr))

def inv_sigmoid(arr):
    return sigmoid(arr)*(1-sigmoid(arr))

for i in range(epochs):
    z=user_mat.dot(prod_mat.T)
    y=sigmoid(z)
    grad=inv_sigmoid(z)
    error=y-labels
    
    user_mat = user_mat - (error*inv_sigmoid(z)).dot(prod_mat)*eta
    prod_mat = prod_mat - ((error*inv_sigmoid(z).T).dot(user_mat)*eta)
    
    if i%5==0:
        print("Updating Database....")
    
    


y=np.round(y)

np.sum(y==labels)/400

np.sum(y)
np.sum(labels)
