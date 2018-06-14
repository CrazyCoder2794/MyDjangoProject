from django.shortcuts import render
from django.http import HttpResponse
from .models import Users,todo
from django.contrib import messages
from django.db import IntegrityError
from django.template import RequestContext

# Create your views here.
def index(request):
	return render(request,'Users/index.html')

def home(request):
	return render(request,'Users/home.html')	

def about(request):
	return render(request,'Users/Aboutus.html')	

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		request.session['username'] = username
		user=Users.objects.get(username=username)
		content = todo.objects.filter(username_id=username)
		try:
			login=Users.objects.get(username=username,password=password)
			return render(request,'Users/my_dashboard.html',{'user':user,'content':content})
		except:
			messages.warning(request, 'Username or password are not matching please check', extra_tags='alert')
	return render(request,'Users/login.html')	

def register(request):
	if request.method == 'POST':
		name = request.POST['name']
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']
		try:
			new_user = Users(name=name, username=username,password=password,email=email)
			new_user.save()
			return render(request,'Users/login.html')
		except IntegrityError:
			messages.warning(request, 'Username already taken please choose something else', extra_tags='alert')
			#return render(request,'Users/register.html')
		
	return render(request,'Users/register.html')


def logout(request):
	try:
		del request.session['username']
	except:
		pass
	return render(request,'Users/logout.html')	

def my_dashboard(request):
	return render(request,'Users/my_dashboard.html')	

def add_task(request):
	if request.method == 'POST':
		task = request.POST['task']
		deadline = request.POST['deadline']
		username = request.session['username']
		
		try:
			new_user = todo(task=task, deadline=deadline,username_id=username)
			new_user.save()
			content = todo.objects.filter(username_id=username)
			return render(request,'Users/my_dashboard.html',{'content':content})
		except:
			messages.warning(request, 'Something went wrong please try again', extra_tags='alert')
			return render(request,'Users/my_dashboard.html')
		
	return render(request,'Users/add_task.html')


def edit_task(request,id):
	request.session['id'] = id
	a=''
	for i in id:
		if i.isdigit():
			a+=i
	content = todo.objects.filter(id=int(a))
	return render(request,'Users/edit_task.html',{'content':content})	

def edit_tas(request):
	if request.method == 'POST':
		task=request.POST['task']
		deadline= request.POST['deadline']
		username = request.session['username']
		try:
			edit_tas=todo(task=task, deadline=deadline,id=request.session['id'],username_id=username)
			edit_tas.save()
			content = todo.objects.filter(username_id=username)
			return render(request,'Users/my_dashboard.html',{'content':content})
		except:
			messages.warning(request, 'Something went wrong please try again', extra_tags='alert')
			content = todo.objects.filter(username_id=username)
			return render(request,'Users/my_dashboard.html',{'content':content})
		
		
def delete_task(request,id):
	request.session['id'] = id
	return render(request,'Users/delete_task.html')	

def del_task(request):
	if request.method == 'POST':
		a=''
		for i in request.session['id']:
			if i.isdigit():
				a+=i
		username = request.session['username']
		#try:
		edit_tas=todo(id=int(a),username_id=username)
		edit_tas.delete()
		content = todo.objects.filter(username_id=username)
		return render(request,'Users/my_dashboard.html',{'content':content})
		'''except:
			messages.warning(request, 'Something went wrong please try again', extra_tags='alert')
			content = todo.objects.filter(username_id=username)
			return render(request,'Users/my_dashboard.html',{'content':content})
		'''
	
	