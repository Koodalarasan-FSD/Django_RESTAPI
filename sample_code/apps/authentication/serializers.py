# apps/authentication/serializers.py

from rest_framework import serializers
from .models import UserCredentials

# Serializer for Login Process
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)

# Serializer for Registration Purpose
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = UserCredentials
        fields = ['username', 'email', 'password1', 'password2']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password1']
        user = UserCredentials.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

# Serializer to Display / Render API Datas
class UserCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCredentials
        fields = ['id', 'password', 'last_login', 'is_superuser', 'username', 'first_name',
                  'last_name', 'is_staff', 'is_active', 'date_joined', 'email',]
        # In Above, Delete fields which is don't wanted to display / render.
