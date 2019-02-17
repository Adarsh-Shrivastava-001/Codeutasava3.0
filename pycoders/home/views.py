from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView,ListView,TemplateView,DetailView

from . models import *
import numpy as np
import pandas as pd

from .dataanalysis import *

def searchbar(request):

	searchterm = request.POST['search']
	products = Product.objects.filter(category__name__icontains=searchterm)
	prod1 = Product.objects.filter(description__icontains=searchterm)
	prod2 = Product.objects.filter(name__icontains=searchterm)
	prod = prod1|prod2|products
	print(prod)
	print('search' , searchterm)
	searchterm='+'.join(searchterm.split(' '))
	print(searchterm)
	map_url="https://www.google.com/search?tbm=lcl&ei=VrtnXIP9M4n_vgTXvaXYDg&q="+searchterm+"+shop+near+me&oq=restaurants+shop+near+me&gs_l=psy-ab.12...0.0.0.11730.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.RHVBknoFfus#rlfi=hd:;si:;mv:!1m2!1d21.2681352!2d81.64117399999999!2m2!1d21.236396799999998!2d81.5739983;tbs:lrf:!2m1!1e2!2m1!1e3!2m1!1e16!2m4!1e17!4m2!17m1!1e2!3sIAE,lf:1,lf_ui:9"

	context = {'product_list':prod,'url_search':map_url}

	return render(request,'home/shop.html',context)




def home(request):
	cat = Category.objects.all()
	product_list = {}
	for c in cat:
		prod = Product.objects.filter(category=c)
		products = []
		for i in range(3):
			products.append(prod[i])
		product_list[c]=products
	print(product_list)



	return render(request,'home/shop_home.html', {'product_list':product_list})

# Create your views here.

def product_detail(request, id):
	product = Product.objects.get(id=id)
	context = {'product':product}
	print(context)
	return render(request,'home/product_detail.html',context)


<<<<<<< HEAD
def update_data(request):

	cust_count = Customer.objects.count()
	print(cust_count)
	user_pro_mat=np.zeros((20,40))
	user_user_mat=np.zeros((20,20))
	user_brand_mat=np.zeros((20,21))
	customer_set=Customer.objects.all()
	for i in range(len(customer_set)):
		print(customer_set[i])
		products=Product.objects.filter(customers=customer_set[i])
		wishlist=Product.objects.filter(customers_wishlist=customer_set[i])
		elec_prod = Product.objects.filter(category__name='Electronics')
		lap_prod = Product.objects.filter(category__name='Laptops')
		mob_prod = Product.objects.filter(category__name='Mobiles')
		shoe_prod = Product.objects.filter(category__name='Shoes')
		acc_prod = Product.objects.filter(category__name='Accessories')
		book_prod = Product.objects.filter(category__name='Electronics')

		cust_elec = products & elec_prod
		cust_lap = products & lap_prod
		cust_mob = products & mob_prod
		cust_shoe = products & shoe_prod
		cust_acc = products & acc_prod
		cust_book = products & book_prod
		category1 = cust_elec | cust_lap | cust_mob #electro or mobile or lap #wt 0
		category2 = cust_shoe | cust_acc #wt 0.6
		category3 = cust_book #wt 0.8
		category4 = wishlist #wt 1

		category1_id = [ cat.id for cat in category1 ]
		category2_id = [ cat.id for cat in category2 ]
		category3_id = [ cat.id for cat in category3 ]
		category4_id = [ cat.id for cat in category4 ]
		print(category1_id)
		print(category2_id)
		print(category3_id)
		print(category4_id)
		# print(cust_elec)
		# print(elec_prod)
		# category1 = []
		# category2 = []
		# category3 = []
		# for j in range(len(products)):
		# 	# print(products[i])
		# 	if products[j].category.name=='Electronics' or 'Laptops' or 'Mobiles':
		# 		print(products[j].category.name,'category1')
		# 		category1.append(j)
		# 	elif products[j].category.name=='Shoes' or 'Accessories':
		# 		category2.append(j)
		# 	elif products[j].category.name=='Books':
		# 		category3.append(j)
		# print(category1,category2,category3)

				

		# prod_ids=[prod.id-1 for prod in products]+[prod.id-1 for prod in wishlist]
		cust_id=customer_set[i].pk
		for j in category1_id:
			user_pro_mat[cust_id-1][j-1]=0
		for j in category2_id:
			user_pro_mat[cust_id-1][j-1]=0.6
		for j in category3_id:
			user_pro_mat[cust_id-1][j-1]=0.8
		for j in category4_id:
			user_pro_mat[cust_id-1][j-1]=1
		


	# for i in range(len(customer_set)):
	# 	friends=Customer.objects.filter(friends=customer_set[i])
	# 	friend_ids=[friend.id for friend in friends]
	# 	cust_id=customer_set[i].pk
	# 	for j in friend_ids:
	# 		user_user_mat[cust_id-1][j-1]=1

	# for i in range(len(customer_set)):
	# 	products=Product.objects.filter(customers=customer_set[i])
	# 	wishlist=Product.objects.filter(customers_wishlist=customer_set[i])
	# 	prod_ids=[prod.brand.id for prod in products]+[prod.brand.id for prod in wishlist]
	# 	cust_id=customer_set[i].pk
	# 	for j in prod_ids:
	# 		user_brand_mat[cust_id-1][j-1]=1





	user_pro_mat=pd.DataFrame(user_pro_mat)
	user_pro_mat.to_pickle('User_Prod_Label.pkl')

	# user_user_mat=pd.DataFrame(user_user_mat)
	# user_user_mat.to_pickle('User_User_Label.pkl')


	# user_brand_mat=pd.DataFrame(user_brand_mat)
	# user_brand_mat.to_pickle('User_Brand_Label.pkl')

=======
from collections import Counter
import numpy as np
import pandas as pd
import operator
>>>>>>> 04f852cf959edacbc800dc203eb6a834fd3959dd

def update_matrix():
	dim=40
	nu=13
	n_p=32


	user_mat=np.random.random((nu,dim))
	prod_mat=np.random.random((n_p,dim))

	labels_up=pd.read_pickle("User_Prod_Label.pkl")
	labels_up=np.array(labels_up)

#	labels_uu=pd.read_pickle("User_User_Label.pkl")
#	labels_uu=np.array(labels_uu)

	epochs=500
	eta=0.01
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
	return user_mat, prod_mat

def get_recommendations(request,id):
    
    user_history = pd.read_pickle('User_Prod_Label.pkl')
    custm = Customer.objects.get(id=id)
    curr_history1 = list(custm.history.all())
    curr_history = [ i.id-1 for i in curr_history1]
    print(curr_history)
    id = id-1
    curr_user_prods = np.array(user_history.iloc[id:(id+1),:])
    current_user_bought = np.where(curr_user_prods>0)[1]
    current_user_wishlist = np.where(curr_user_prods==1)[1]
    # curr_history = set(current_user_bought.tolist())
    # curr_history = list(curr_history)
    count_arr=[]
    for i in range(20):
        
        user_vect, product_vect = update_matrix()    
        user = user_vect[0]
        user = np.reshape(user,(1,40))
        score = np.dot(user,product_vect.T)
        ind = np.argsort(score)[0]
        ind_new = []
        nind_new=[]
        for i in ind:
        	if i not in curr_history:
        		ind_new.append(i)
        for i in ind_new:
        	if i not in current_user_wishlist:
        		nind_new.append(i)


        # ind_new = [ i for i in ind if i not in curr_history and i not in current_user_wishlist ]
        count_arr.append(nind_new[-10:])
    
    freq_arr = []
    for j in range(20):
        for i in count_arr[j]:
            freq_arr.append(i)
    
    c = Counter(freq_arr)
    sorted_c = sorted(c.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_c)
    results = []
    counter=0
    for item in sorted_c:
        if counter>5 or item[1]<10:
            break
        else:
            results.append(item[0])
            counter+=1
    print(results)
            
    product_list = []
    wish_list = []
    for w in current_user_wishlist:
    	wish = Product.objects.get(id=w+1)
    	wish_list.append(wish)
    for  r in results:
        prod = Product.objects.get(id=r+1)
        product_list.append(prod)
    print(product_list)
    print(wish_list)
    return render(request,'home/recommend.html',{'product_list':product_list,'wish_list':wish_list})


def update_data(request):

	cust_count = Customer.objects.count()
	product_count = Product.objects.count()
	print(product_count)
	user_pro_mat=np.zeros((cust_count,product_count))
	customer_set=Customer.objects.all()
	for i in range(len(customer_set)):
		print(customer_set[i])
		products=Product.objects.filter(customers=customer_set[i])
		wishlist=Product.objects.filter(customers_wishlist=customer_set[i])
		elec_prod = Product.objects.filter(category__name='Electronics')
		lap_prod = Product.objects.filter(category__name='Laptops')
		mob_prod = Product.objects.filter(category__name='Mobiles')
		shoe_prod = Product.objects.filter(category__name='Shoes')
		acc_prod = Product.objects.filter(category__name='Accessories')
		book_prod = Product.objects.filter(category__name='Books')

		cust_elec = products & elec_prod
		cust_lap = products & lap_prod
		cust_mob = products & mob_prod
		cust_shoe = products & shoe_prod
		cust_acc = products & acc_prod
		cust_book = products & book_prod
		category1 = cust_elec | cust_lap | cust_mob #electro or mobile or lap #wt 0
		category2 = cust_shoe | cust_acc #wt 0.6
		category3 = cust_book #wt 0.8
		category4 = wishlist #wt 1
		print(category1)
		print(category2)
		print(category3)
		print(category4)
	

		category1_id = [ cat.id for cat in category1 ]
		category2_id = [ cat.id for cat in category2 ]
		category3_id = [ cat.id for cat in category3 ]
		category4_id = [ cat.id for cat in category4 ]
		print(category1_id)
		print(category2_id)
		print(category3_id)
		print(category4_id)

		cust_id=customer_set[i].pk
		for j in category1_id:
			user_pro_mat[cust_id-1][j-1]=0
		for j in category2_id:
			user_pro_mat[cust_id-1][j-1]=0.4
		for j in category3_id:
			user_pro_mat[cust_id-1][j-1]=0.6
		for j in category4_id:
			user_pro_mat[cust_id-1][j-1]=1.2
	user_pro_mat=pd.DataFrame(user_pro_mat)
	user_pro_mat.to_pickle('User_Prod_Label.pkl')


# def update_matrix():
# 	dim=10
# 	nu=20
# 	n_p=40


# 	user_mat=np.random.random((nu,dim))
# 	prod_mat=np.random.random((n_p,dim))

# 	labels_up=pd.read_pickle("User_Prod_Label.pkl")
# 	labels_up=np.array(labels_up)

# 	labels_uu=pd.read_pickle("User_User_Label.pkl")
# 	labels_uu=np.array(labels_uu)

# 	epochs=500
# 	eta=0.005
# 	lam=0.01

# 	def sigmoid(arr):
# 	    return 1/(1+np.exp(-1*arr))

# 	def inv_sigmoid(arr):
# 	    return sigmoid(arr)*(1-sigmoid(arr))

# 	for i in range(epochs):
# 	    z_up=user_mat.dot(prod_mat.T)
# 	    y_up=sigmoid(z_up)
# 	    grad_up=inv_sigmoid(z_up)
# 	    error_up=y_up-labels_up

# 	    user_mat = user_mat - (error_up*grad_up).dot(prod_mat)*eta
# 	    prod_mat = prod_mat - ((error_up*grad_up).T).dot(user_mat)*eta
# 	return user_mat, prod_mat

# 	for i in range(epochs*2):
# 	    z_uu=user_mat.dot(user_mat.T)
# 	    y_uu=sigmoid(z_uu)
# 	    grad_uu=inv_sigmoid(z_uu)
# 	    error_uu=y_uu-labels_uu

# 	    user_mat = user_mat - (error_uu*grad_uu).dot(user_mat)*eta
# 	    user_mat = user_mat - ((error_uu*grad_uu).T).dot(user_mat)*eta

# 	for i in range(epochs*2):

# 	    z_ub=user_mat.dot(brand_mat.T)
# 	    y_ub=sigmoid(z_ub)
# 	    grad_ub=inv_sigmoid(z_ub)
# 	    error_ub=y_ub-labels_ub

# 	    user_mat = user_mat - (error_ub*grad_ub).dot(brand_mat)*eta
# 	    brand_mat = brand_mat - ((error_ub*grad_ub).T).dot(user_mat)*eta

# 	    if i%5==0:
# 	        print("Updating Database....")

<<<<<<< HEAD
# class ListHome(ListView):
# 	update_data()
# 	model=Customer
# 	template_name="home/home.html"
=======

# def recommend_prod(pk):
# 	relation=read_pickle('user_prod.pkl')
# 	poss_prods=np.argsort(relation[pk+1])
# 	return poss_prods

# def recommend_user(pk):
# 	relation=read_pickle('user_user.pkl')
# 	poss_friends=np.argsort(relation[pk+1])
# 	return poss_friends

# def recommend_user(pk):
# 	relation=read_pickle('user_brand.pkl')
# 	poss_brands=np.argsort(relation[pk+1])
# 	return poss_brands


# # class ListHome(ListView):
# # 	update_data()
# # 	model=Customer
# # 	template_name="home/home.html"
>>>>>>> 04f852cf959edacbc800dc203eb6a834fd3959dd




def shop(request):
	return render(request,'home/shop.html')

# def sprod(request):
# 	product = Product.objects.all()
# 	l = Product.objects.count()
# 	description = [ p.name+" "+p.search for p in product ]
# 	desc = pd.DataFrame(description)
# 	desc.to_pickle('descriptions.pkl')
# 	print(description)




