from rest_framework import serializers
from django.contrib.auth.models import User
from myapp.models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        fields = ('username', 'email','password','role')

    def create(self, validated_data):
        role_name = validated_data.pop('role', None)
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])  # ✅ Hash the password
        user.save()

        if role_name:
            role, created = Role.objects.get_or_create(name=role_name)
            UserRole.objects.create(user=user, role=role)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True, write_only =True)

