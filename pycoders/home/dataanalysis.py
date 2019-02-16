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
