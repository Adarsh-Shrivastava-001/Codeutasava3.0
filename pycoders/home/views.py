from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView,ListView,TemplateView,DetailView

from . models import *
import numpy as np
import pandas as pd

def searchbar(request):
<<<<<<< HEAD
	searchterm = request.POST['search'].lower()
	print(searchterm)
	products=Product.objects.all()
	req_list=[]
	for product in products:
		print(product.category.all()[0])
		if searchterm in (product.description+product.name):
			req_list.append(product)
	print(req_list)


	
	context = {'product_list':req_list,'category':searchterm}
=======
	searchterm = request.POST['search']
	products = Product.objects.filter(category__name__icontains=searchterm)

	# print(products)
	prod1 = Product.objects.filter(description__icontains=searchterm)
	prod2 = Product.objects.filter(name__icontains=searchterm)
	prod = prod1|prod2|products
	print(prod)
	# req_list=[]
	# for product in products:
	# 	# print(product)
	# 	cat = product.category_set.all()
	# 	print(cat)
	# 	if searchterm in product.description:
	# 		#print(product.category)
	# 		req_list.append(product)

	# print(product)
	searchterm = [ p.search.name for p in prod]
	print(searchterm)
	
	context = {'product_list':prod,'category':searchterm}
>>>>>>> 764b8743c4dd00e5c694ab3b6d99df3f760a8e04
	return render(request,'home/product_detail.html',context)
	
	


def home(request):
	return render(request,'home/home.html')
	
# Create your views here.

def update_data():
	user_pro_mat=np.zeros((20,40))
	user_user_mat=np.zeros((20,20))
	user_brand_mat=np.zeros((20,21))
	customer_set=Customer.objects.all()
	for i in range(len(customer_set)):
		products=Product.objects.filter(customers=customer_set[i])
		wishlist=Product.objects.filter(customers_wishlist=customer_set[i])
		prod_ids=[prod.id-1 for prod in products]+[prod.id-1 for prod in wishlist]
		cust_id=customer_set[i].pk
		for j in prod_ids:
			user_pro_mat[cust_id-1][j-1]=1

	for i in range(len(customer_set)):
		friends=Customer.objects.filter(friends=customer_set[i])
		friend_ids=[friend.id for friend in friends]
		cust_id=customer_set[i].pk
		for j in friend_ids:
			user_user_mat[cust_id-1][j-1]=1

	for i in range(len(customer_set)):
		products=Product.objects.filter(customers=customer_set[i])
		wishlist=Product.objects.filter(customers_wishlist=customer_set[i])
		prod_ids=[prod.brand.id for prod in products]+[prod.brand.id for prod in wishlist]
		cust_id=customer_set[i].pk
		for j in prod_ids:
			user_brand_mat[cust_id-1][j-1]=1





	user_pro_mat=pd.DataFrame(user_pro_mat)
	user_pro_mat.to_pickle('User_Prod_Label.pkl')

	user_user_mat=pd.DataFrame(user_user_mat)
	user_user_mat.to_pickle('User_User_Label.pkl')


	user_brand_mat=pd.DataFrame(user_brand_mat)
	user_brand_mat.to_pickle('User_Brand_Label.pkl')





def update_matrix():
	dim=10
	nu=20
	n_p=40


	user_mat=np.random.random((nu,dim))
	prod_mat=np.random.random((n_p,dim))

	labels_up=pd.read_pickle("User_Prod_Label.pkl")
	labels_up=np.array(labels_up)

	labels_uu=pd.read_pickle("User_User_Label.pkl")
	labels_uu=np.array(labels_uu)

	epochs=500
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

	        
	for i in range(epochs*2):
	    z_uu=user_mat.dot(user_mat.T)
	    y_uu=sigmoid(z_uu)
	    grad_uu=inv_sigmoid(z_uu)
	    error_uu=y_uu-labels_uu
	    
	    user_mat = user_mat - (error_uu*grad_uu).dot(user_mat)*eta
	    user_mat = user_mat - ((error_uu*grad_uu).T).dot(user_mat)*eta

	for i in range(epochs*2):
    
	    z_ub=user_mat.dot(brand_mat.T)
	    y_ub=sigmoid(z_ub)
	    grad_ub=inv_sigmoid(z_ub)
	    error_ub=y_ub-labels_ub
	    
	    user_mat = user_mat - (error_ub*grad_ub).dot(brand_mat)*eta
	    brand_mat = brand_mat - ((error_ub*grad_ub).T).dot(user_mat)*eta
	    
	    if i%5==0:
	        print("Updating Database....")



def recommend_prod(pk):
	relation=read_pickle('user_prod.pkl')
	poss_prods=np.argsort(relation[pk+1])
	return poss_prods

def recommend_user(pk):
	relation=read_pickle('user_user.pkl')
	poss_friends=np.argsort(relation[pk+1])
	return poss_friends

def recommend_user(pk):
	relation=read_pickle('user_brand.pkl')
	poss_brands=np.argsort(relation[pk+1])
	return poss_brands


class ListHome(ListView):
	update_data()
	model=Customer
	template_name="home/home.html"
