from nturl2path import url2pathname
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main_site, name='main_site'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.log_out, name='log_out'),
    path('profile/',views.profile, name='profile'),
    path('profile/update_user_contact_info', views.update_user_contact_info, name='update_user_contact_info'),
    path('login/', views.log_in, name='login'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
    path('post_deleted/<int:pk>', views.delete_post, name='delete_post'),
    path('details/<int:pk>',views.details, name='details'),
    path('er_auth/', views.er_auth, name='er_auth')
]