# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserCredentials(AbstractUser):
    pass


    """
    We have to mention id, username, password, email but we don't...Because In Django, when you extend 
    the AbstractUser class to create a custom user model, you inherit all the fields and methods of the 
    default User model, including username and password,email,firstname and lastname. 
    Therefore, you don't need to explicitly define these fields again in your custom user model unless 
    you want to add additional fields or override(customizing) the existing ones.

    """
    
    """
    Please check settings.py, we mentioned above model as Custom User Model
    """
    