from nturl2path import url2pathname
from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_site, name='main_site'),
    path('signup/', views.signup, name='signup'),
    path('auth/', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='log_out'),
    path('edit_profile/',views.edit_profile, name='edit_profile')
]