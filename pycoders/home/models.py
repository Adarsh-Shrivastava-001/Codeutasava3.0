from django.db import models

from django.contrib.auth.models import User

import datetime


# Create your models here.

class DataAnalyst(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	user_type = models.CharField(max_length=2,blank=True, null=True, default='DA')

	def __str__(self):
		return self.user.username


class Customer(models.Model):
	first_name=models.CharField(max_length=25,blank=True,null=True)
	last_name=models.CharField(max_length=25,blank=True,null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='static/uploads/avatar', null=True, blank=True)
	email=models.EmailField(max_length=70,blank=True,null=True)
	contact_no=models.IntegerField(null=True)
	address=models.CharField(max_length=100, blank=True,null=True)
	city=models.CharField(max_length=100, blank=True,null=True)
	dob= models.DateTimeField(blank=True,null=True)
	history=models.ManyToManyField('Product', related_name='customers', blank=True,null=True)
	friends=models.ManyToManyField('Customer', related_name='_friends', blank=True,null=True)
	wishlist=models.ManyToManyField('Product', related_name='customers_wishlist', blank=True,null=True)
	ineterests = models.ManyToManyField('Category', related_name='customers_interests', blank=True,null=True)

	def __str__(self):
		return self.first_name + " " + self.last_name

# class SearchTerm(models.Model):
# 	name = models.CharField(max_length=100,blank=True, null=True)

# 	def __str__(self):
# 		return self.name

class Product(models.Model):
	name=models.CharField(max_length=100,blank=True)
	brand=models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='products', blank=True)
	image = models.ImageField(upload_to='static/uploads/product', null=True, blank=True)
	image1 = models.ImageField(upload_to='static/uploads/product', null=True, blank=True)
	image2 = models.ImageField(upload_to='static/uploads/product', null=True, blank=True)
	category=models.ManyToManyField('Category', related_name='products', blank=True,null=True)
	description=models.TextField(blank=False, null=False)
	price=models.IntegerField(null=True)
	dicount=models.FloatField(null=True)
	rating=models.IntegerField(null=True)
	review = models.ManyToManyField('Review', related_name='product_review', blank=True, null=True)
	delivery=models.IntegerField(null=True)
	search = models.CharField(max_length=200, blank=True, null=True)
	history=models.ManyToManyField('Customer',related_name='products', blank=True,null=True) #To store the users who viewed th product
	

	def __str__(self):
		return self.name

class Brand(models.Model):
	name=models.CharField(max_length=100,blank=True)
	image = models.ImageField(upload_to='static/uploads/brand', null=True, blank=True)
	categories_active=models.ManyToManyField('Category', related_name='brands', blank=True, null=True)
	customers=models.ManyToManyField('Customer', related_name='brands', blank=True, null=True)
	rating=models.FloatField(blank=True, null=True)	

	def __str__(self):
		return self.name

class Category(models.Model):
	name=models.CharField(max_length=25)

	def __str__(self):
		return self.name

class Store(models.Model):
	name=models.CharField(max_length=50)
	location=models.CharField(max_length=50)
	email=models.EmailField()
	contact_no=models.IntegerField()
	brand=models.ManyToManyField('Brand', related_name='stores')
	customers=models.ManyToManyField('Customer', related_name='stores')

	def __str__(self):
		return self.name



class TimeStamp(models.Model):
	date=models.DateField(default=datetime.datetime.now())
	customer=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='date', blank=True,null=True)
	product=models.ForeignKey('Product', on_delete=models.CASCADE, related_name='date', blank=True,null=True)


class Review(models.Model):
	review = models.TextField()

	def __str__(self):
		return self.review