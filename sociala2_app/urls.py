from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('register/', views.registerPage, name='register'),
path('accounts/login/', views.loginPage, name='login'),
path('logout/', views.logoutPage, name='logout'),

path('socials/', views.social_list, name='social-list'),
path('socials/<int:id>/', views.social_detail, name='social-detail'),

path('socials/create/', views.create_social, name='social-create'),
path('socials/<int:id>/update/', views.update_social, name='social-update'),
path('socials/<int:id>/delete/', views.delete_social, name='social-delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)