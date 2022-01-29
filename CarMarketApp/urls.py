from nturl2path import url2pathname
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main_site, name='main_site'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.log_out, name='log_out'),
    path('profile/',views.profile, name='profile'),
    path('login/', views.log_in, name='login'),
    path('add_post/', views.add_post, name='add_post')
]