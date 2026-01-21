from django.contrib import admin
from django.contrib.auth import get_user_model 
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import UserProfile

User = get_user_model()

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user__username', 'bio',)
    search_fields = ('id', 'user__username')
    list_filter = ('user',)
    
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    extra = 0
    
admin.site.unregister(User)

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    inlines = [UserProfileInline]