from django.shortcuts import render
import pandas as pd

# Create your views here.

from home.dataanalysis import *


def user_cluster(request):
	dataset=pd.read_pickle("User_Prod_Label.pkl")
	cluster(dataset, 'essence_')
	return render(request, 'data_analysis/user_cluster.html')

def time_graph(request):
	# dataset=pd.read_pickle("User_Prod_Label.pkl")
	# plot_time_graph(dataset, 'essence', color_l="blue", color_p="red")
	return render(request, 'data_analysis/time_revenue.html')


def dashboard(request):
	return render(request,'data_analysis/index.html')

def third_party(request):
	csv_file='test.csv'
	csv_np=csv_to_numpy(csv_file)
	mat=user_embedding(csv_np)
	cluster(mat, 'third__')
	return render(request, 'data_analysis/user_cluster_third.html')

