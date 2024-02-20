from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from .models import Post
from .forms import LoginForm, RegisterForm, PostForm
import psycopg2
import environ
import logging
import re

# Environ stuff
env = environ.Env()
environ.Env.read_env()

# # Create your views here.
# def say_hello(request):
#     # return HttpResponse('Hello, World!')
#     x = 1
#     y = 2
#     return render(request, 'hello.html', {'name': 'Test'})

# def dummy_insert(request):
#     # return HttpResponse(request.GET.get('input'))
#     columns = ['first_name', 'last_name', 'gender', 'date_of_birth', 'email']
#     values = [f'\'{value}\'' for value in request.GET.get('input').split(', ')]
#     values[3] = f'DATE{values[3]}'
#     table = 'person'

#     # Begin PostgreSQL stuff
#     conn = psycopg2.connect(host=env("DB_HOST"), dbname=env("DB_NAME"), user=env("DB_USER"), password=env("DB_PASSWORD"), port=env("DB_PORT"))
#     cur = conn.cursor()

#     cur.execute(f"""
#         INSERT INTO {table} ({', '.join(column for column in columns)})
#         VALUES ({', '.join(value for value in values)})
#     """)

#     conn.commit()
#     cur.close()
#     conn.close()
#     # End PostgreSQL stuff

#     return HttpResponse(f'inserted ({ columns }) into person values ({ values })')

def default_view(request):
    if request.method == 'GET':
        return redirect('home')

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Registration successful')
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})
    
def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi, {username.title()}, welcome back!')
                return redirect('home')
    
    messages.error(request, 'Invalid username or password')
    return render(request, 'login.html', {'form': form})

def sign_out(request):
    if request.method == 'GET':
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('login')
    
    
@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'post_form.html', context)
    
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            messages.success(request, 'The post has been created successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'post_form.html', {'form': form})
        

@login_required
def create_post_norefresh(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        
        new_post = Post(title=title, content=content, author=author)
        new_post.save()
        
        # Currently suppressing the messages in the no-refresh view,
        # as that leads to the accumulation of messages that are only shown upon refresh.
        # TODO: restore the functionality after introducing a header to the HTML pages.
        # success = 'New comment created successfully'
        # messages.success(request, success)
        
        # Building a response
        # TODO: switch the serializer to that of the Django REST framework
        post_array = serializers.serialize('json', [new_post])
        response = post_array[1:-1]
        
        response = re.sub(r'"author": \d+', f'"author": "{request.user.username}"', response)
        
        logging.warning(response)
        logging.warning(request.user.username)
        
        return HttpResponse(response, content_type='application/json')
        
        
@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'id': id}
        return render(request, 'post_form.html', context)
    
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the following error:')
            return render(request, 'post_form.html', {'form': form})
        

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post': post}
    
    if request.method == 'GET':
        return render(request, 'post_confirm_delete.html', context)
    
    elif request.method == 'POST':
        post.delete()
        messages.success(request, 'The comment has been deleted successfully.')
        return redirect('home')
        

def home(request):
    posts = Post.objects.all().order_by('-published_at')
    context = {'posts': posts, 'form': PostForm()}
    
    if request.method == 'GET':
        return render(request, 'home.html', context)
    
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            messages.success(request, 'The post has been created successfully.')
            return render(request, 'home.html', context)
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'home.html', context)
    

def about(request):
    return render(request, 'about.html')