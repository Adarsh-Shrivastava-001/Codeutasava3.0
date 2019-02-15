from django.shortcuts import render
from . models import *
import numpy as np
import pandas as pd

# Create your views here.

def update_data():
	mat=np.zeros((20,40))
	customer_set=Customer.objects.all()
	for i in range(len(customer_set)):
		products=Products.objects.filter(customers=customer_set[i])
		prod_ids=[prod.id-1 for prod in products]
		for j in prod_ids:
			mat[cust_id-1,j-1]=1
	mat=pd.DataFrame(mat)
	mat.to_pickle('data.pkl')





