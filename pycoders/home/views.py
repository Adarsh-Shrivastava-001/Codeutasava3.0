from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView,ListView,TemplateView,DetailView



from . models import *
import numpy as np
import pandas as pd

# Create your views here.

def update_data():
	user_pro_mat=np.zeros((20,40))
	customer_set=Customer.objects.all()
	for i in range(len(customer_set)):
		products=Product.objects.filter(customers=customer_set[i])
		wishlist=Product.objects.filter(customers_wishlist=customer_set[i])
		prod_ids=[prod.id-1 for prod in products]+[prod.id-1 for prod in wishlist]
		cust_id=customer_set[i].pk
		for j in prod_ids:
			user_pro_mat[cust_id-1][j-1]=1

	for i in range(len(customer)):
		pass

	user_pro_mat=pd.DataFrame(mat)
	user_pro_mat.to_pickle('User_Prod_Label.pkl')




class ListHome(ListView):
	update_data()
	model=Customer
	template_name="home/home.html"
