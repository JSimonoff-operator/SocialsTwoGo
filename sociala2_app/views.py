from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from .models import *   #import all the models
from django.views import generic #so that we can inherit genric view stuff
from .forms import * #import all of our forms
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
# Create your views here.
def index(request):
# Render index.html
    return render( request, 'sociala2_app/index.html')

class SocialListView(generic.ListView):
    model = SocialAccount
    context_object_name = 'social_list'

class SocialDetailView(generic.ListView):
    model = SocialAccount
    context_object_name = 'social_detail'

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user =  form.cleaned_data.get('username')
                messages.success(request, 'Account Created for ' + user + '.')
                return redirect('login')

        context = {'form':form}
        return render(request, 'sociala2_app/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password = password)

                if user is not None:
                    login(request, user)
                    return redirect("index")
                else:
                    messages.info(request, 'Username OR Password is incorrect')
                    return render(request, 'sociala2_app/registration/login.html', context )

        context = {'loginform':form}
        return render(request, 'sociala2_app/registration/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')


def social_list(request):
    social = SocialAccount.objects.all()
    return render( request, 'sociala2_app/social_list.html',
                   {'social': social})


def social_detail(request, id): # note the additional id parameter
   social = SocialAccount.objects.get(id=id)
   return render(request,
          'sociala2_app/social_details.html',
         {'social': social})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Influencer'])
def create_social(request):
    if request.method == 'POST':
        form = SocialAccountForm(request.POST)
        if form.is_valid():
            # create a new `social` and save it to the dbsqlite3
            social = form.save()
            # Redirect to the social-list upon completion
            return redirect('social-list')
    else:
        form = SocialAccountForm()

    return render(request,
                'sociala2_app/create_social.html',
                {'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Influencer'])
def update_social(request, id):
    social = SocialAccount.objects.get(id=id)
    if request.method == 'POST':
        form = SocialAccountForm(request.POST, instance=social)
        if form.is_valid():
            # update the existing `social` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('social-list')
    else:
        form = SocialAccountForm(instance=social)

    return render(request,
                'sociala2_app/update_social.html',
                {'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Influencer'])
def delete_social(request, id):
    social = SocialAccount.objects.get(id=id) # we need this for both GET and POST

    if request.method == 'POST':
        # delete the social from the database
        social.delete()
        # redirect to the social list
        return redirect('social-list')

    # no need for an `else` here. If it's a GET request, just continue

    return render(request,
                    'sociala2_app/delete_social.html',
                    {'social': social})