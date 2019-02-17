#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 23:18:50 2019

@author: adarsh
"""

from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
import pandas as pd
import numpy as np

def find_optimum_n(x1,x2, brand):
    # plt.title('Dataset')
    # plt.scatter(x1, x2)
    # plt.show()
    
    # # create new plot and data
    # plt.plot()
    X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
    
    # k means determine k
    distortions = []
    K = range(1,10)
    for k in K:
        kmeanModel = KMeans(n_clusters=k).fit(X)
        kmeanModel.fit(X)
        distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
    
    slopes = []
    for i in range(len(distortions)-1):
        y_grad = distortions[i+1]-distortions[i]
        x_grad = 1
        slope = y_grad/x_grad
        slopes.append(slope)
        
    slope_grad = []
    for i in range(len(slopes)-1):
        grad = slopes[i+1]-slopes[i]
        slope_grad.append(grad)
    
    pivot = max(slope_grad)
    n_optimum = slope_grad.index(pivot)+2
    
        
    # Plot the elbow
    plt.plot(K, distortions, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Distortion')
    plt.title('The Elbow Method showing the optimal k')
    plt.savefig("static/graphs/"+brand+'elbow.jpg')
    plt.close()
    return n_optimum

def cluster(user_embeddings,brand):
   
    pca = TruncatedSVD(n_components=2)
    reduced_user_embeddings = pca.fit_transform(user_embeddings)
    x = [  reduced_user_embeddings[i][0] for i in range(20)]
    y = [ reduced_user_embeddings[i][1] for i in range(20) ]
    x1 = np.array(x)
    x2 = np.array(y)   
    n = find_optimum_n(x1,x2, brand)
    
    kmeans = KMeans(n_clusters=n)
    user_cluster = kmeans.fit_predict(reduced_user_embeddings)
    plot_clusters(user_cluster,x,y,brand)

    

def plot_clusters(user_cluster,x,y, brand):
    for i in range(len(x)):
        x_ = x[i]
        y_ = y[i]
        c = user_cluster[i]
        col = ['red','blue','green','brown','purple']
        plt.scatter(x_,y_, color=col[c])
#
    plt.savefig("static/graphs/"+brand+'clusters.jpg')
    plt.close()
    
# cluster(user_mat, 'z')



def plot_time_graph(inp, brand_name, color_l="blue", color_p="red"):
    x=inp[0]
    y=inp[1]
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.plot(x,y, color=color_l)
    plt.scatter(x,y, color=color_p)
    plt.savefig("static/graphs/"+brand_name+"_time.jpg")


def csv_to_numpy(csv_file):
    new_data=pd.read_csv(csv_file)
    mat=np.array(new_data)

    max_=np.max(mat)
    new_mat=np.zeros((len(mat),max_))

    for i in range(len(mat)):
        for j in range(max_):
            if j in mat[i][1:]:
                new_mat[i][j]=1
    return new_mat



def user_embedding(mat):
    dim=10
    nu,n_p=np.shape(mat)


    user_mat=np.random.random((nu,dim))
    prod_mat=np.random.random((n_p,dim))

    labels_up=mat



    epochs=1000
    eta=0.005
    lam=0.01

    def sigmoid(arr):
        return 1/(1+np.exp(-1*arr))

    def inv_sigmoid(arr):
        return sigmoid(arr)*(1-sigmoid(arr))

    for i in range(epochs):
        z_up=user_mat.dot(prod_mat.T)
        y_up=sigmoid(z_up)
        grad_up=inv_sigmoid(z_up)
        error_up=y_up-labels_up

        user_mat = user_mat - (error_up*grad_up).dot(prod_mat)*eta
        prod_mat = prod_mat - ((error_up*grad_up).T).dot(user_mat)*eta

    return user_mat





      