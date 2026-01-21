from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import UserProfile


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "date_joined",
            "password",
        ]
        read_only_fields = ["id","date_joined","is_active","is_staff"]
        
        def create(self, validated_data):
            password = validated_data.pop('password',None)
            user = User(**validated_data)
            if password:
                user.set_password(password)
            else:
                user.set_unusable_password()
            user.save()
            return user
        
        def upddate(self, instance, validated_data):
            password = validated_data.pop("password", None)
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            if password:
                instance.set_password(password)
            instance.save()
            return instance
        
class UserProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all(), write_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = UserProfile
        fields = [
            "id",
            "user_id",
            "username",
            "photo",
            "bio",
        ]