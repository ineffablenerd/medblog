from django.shortcuts import render,redirect
from .models import *
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
	home = Home.objects.all()
	allPost = Post.objects.all()
	RecentPost = Post.objects.all()[::-1]
	context = {'home':home,'posts':allPost,'recentpost':RecentPost}
	return render(request,'blog/index.html',context)


def blog(request):
	home = Home.objects.all()
	allPost = Post.objects.all()[::-1]
	context = {'home':home,'posts':allPost}
	return render(request,'blog/blog.html',context)

def contact(request):
	home = Home.objects.all()
	context = {'home':home}

	if request.method == "POST":
		firstname = request.POST['fname']
		lastname = request.POST['lname']
		email  = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']

		if len(firstname) > 4:
			contact = Contact(first_name=firstname,last_name=lastname,email=email,subject=subject,message=message)
			contact.save()
			messages.success(request,'Successfully Form Submit')
			return redirect('/contact')
		else:
			messages.error(request,'First Name Should Be more then 4 chars')
			return redirect('/contact')


	return render(request,'blog/contact.html',context)


def single(request,slug):
	home = Home.objects.all()
	post = Post.objects.filter(slug=slug).first()

	comment = Comment.objects.filter(post=post)
	

	if request.method == "POST":
		name = request.user.get_full_name()
		email = request.user.email
		postsno = request.POST.get('postsno')
		message = request.POST['message']

		if postsno:
			post_data = Post.objects.get(sno=postsno)
			new_comment = Comment(name=name, email=email, post=post_data, message=message)
			new_comment.save()
			messages.success(request, "Comment Successfully Submitted")
			return redirect('/')
		else:
			messages.error(request, "Post ID is missing")


	context = {'home':home,'post':post,'comment':comment}
	return render(request,'blog/single.html',context)


	


def login(request):
	if request.user.is_authenticated:
		return  redirect('/')

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		print(password)

		user = authenticate(request,username=username,password=password)
		print(user)
		if user is not None:
			auth_login(request,user)
			messages.success(request,"Successfully Login")
			return redirect('/')
		else:
			messages.error(request,"Something Went Wrong")
			return redirect('/login')
	return render(request,'auth/login.html')

def signup(request):
	if request.user.is_authenticated:
		return  redirect('/')

	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']

		
		username_check = User.objects.filter(username=username).exists()
		email_check = User.objects.filter(email=email).exists()
		
		if username_check == True:
			messages.error(request,"Username Already Exists")
			return redirect('/signup')
		
		if email_check == True:
			messages.error(request,"Your Email Already Exists")
			return redirect('/signup')


		if len(username) >= 15:
			messages.error(request,'Username Too Long')
			return redirect('/signup')
		
		elif password != cpassword:
			messages.error(request,"Password And Confirm Did'nt Match")
			return redirect('/signup')

		else:
			user = User.objects.create_user(username=username,email=email,password=cpassword)
			user.first_name = fname 
			user.last_name = lname 
			user.save()
			messages.success(request,"Your Account Successfully Created")
			return redirect('/login')


	return render(request,'auth/signup.html')

def add_post(request):
	home = Home.objects.all()
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)  # Note the request.FILES to handle file uploads
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user.username
			post.email = request.user.email  # Set the author field to the logged-in user's userna
			post.save()
			messages.success(request, 'Post created successfully')
			return redirect('home')  # Redirect to a success page or the new post's page
		else:
			messages.error(request, 'Error creating post')
	else:
		form = PostForm()
	context = {'home': home, 'form': form}
	return render(request, 'blog/add_post.html', {'form': form})
	

def logout(request):
	auth_logout(request)
	messages.success(request,"Logout Succesfully")
	return redirect('/')