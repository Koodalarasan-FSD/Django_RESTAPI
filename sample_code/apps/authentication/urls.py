# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, logout,list_users,jsonlist_users,jsonlist_users_by_id,list_users_by_id
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", logout, name="logout"),
    path("list_users",list_users,name='list_users'),
    path("list_users/<int:user_id>",list_users_by_id,name='list_users_by_id'),
    path("jsonlist_users",jsonlist_users,name='jsonlist_users'),
    path("jsonlist_users/<int:user_id>",jsonlist_users_by_id,name='jsonlist_users_by_id')
    
]
