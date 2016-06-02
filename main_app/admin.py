from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import *

class AbstractUserInline(admin.StackedInline):
    model = AbstractUser
    can_delete = False
    verbose_name_plural = 'AbstractUser'

class UserAdmin(BaseUserAdmin):
    inlines = (AbstractUserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
