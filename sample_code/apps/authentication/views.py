# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import LoginForm, SignUpForm
from .models import UserCredentials
from .serializers import UserCredentialsSerializer
from django.http import JsonResponse, Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework.decorators import api_view


# Below function is to view(render) login page and also for logining Process
@api_view(['GET', 'POST'])
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect("/")
        else:
            msg = 'Invalid credentials'
            return render(request, "accounts/login.html", {"form": form, "msg": msg})

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

# Below function is to view(render) register page and also for registering Process
@api_view(['GET', 'POST'])
def register_user(request):
    msg = None
    success = False
    form = SignUpForm(request.POST)

    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            username = serializer.validated_data.get("username")
            raw_password = serializer.validated_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

# For Logout Process
@api_view(['POST'])
def logout(request):
    auth_logout(request)
    return redirect('/')

# Rendering API Datas on Django Admin Interface
@api_view(['GET'])
def list_users(request):
    users = UserCredentials.objects.all()
    serializer = UserCredentialsSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Rendering API Specific Datas on Django Admin Interface
@api_view(['GET'])
def list_users_by_id(request, user_id):
    try:
        user = UserCredentials.objects.get(pk=user_id)
    except UserCredentials.DoesNotExist:
        raise Http404("User not found")

    serializer = UserCredentialsSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Rendering API Datas directly on Web Page as JSON
@api_view(['GET'])
def jsonlist_users(request):
    users = UserCredentials.objects.all()
    serializer = UserCredentialsSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)

# Rendering API Specific Datas directly on Web Page as JSON
@api_view(['GET'])
def jsonlist_users_by_id(request, user_id):
    try:
        user = UserCredentials.objects.get(pk=user_id)
    except UserCredentials.DoesNotExist:
        raise Http404("User not found")

    serializer = UserCredentialsSerializer(user)
    return JsonResponse(serializer.data, safe=False)
