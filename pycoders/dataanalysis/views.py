from django.shortcuts import render
import pandas as pd

# Create your views here.

from home.dataanalysis import *


def user_cluster(request):
	dataset=pd.read_pickle("User_Prod_Label.pkl")
	cluster(dataset, 'essence_')
	return render(request, 'data_analysis/user_cluster.html')

def time_graph(request):
	dataset=pd.read_pickle("User_Prod_Label.pkl")
	plot_time_graph(dataset, 'essence', color_l="blue", color_p="red")
	return render(request, 'data_analysis/time_revenue.html')



