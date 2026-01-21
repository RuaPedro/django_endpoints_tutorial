from django.conf import settings # Import Settings to acces AUTH_USER_MODEL
from django.db import models 

# Profile model linked to the User model
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    bio = models.TextField(blank=True)