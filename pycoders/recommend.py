#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:20:38 2019

@author: adarsh
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



user_mat=np.random.random((20,10))
prod_mat=np.random.random((40,10))

labels=pd.read_pickle("User_Prod_Label.pkl")
labels=np.array(labels)

epochs=500
eta=0.005
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
    prod_mat = prod_mat - ((error*inv_sigmoid(z)).T).dot(user_mat)*eta
    
    if i%5==0:
        print("Updating Database....")
    
    


np.sum(np.round(y)==labels)/800


q=np.round(y)