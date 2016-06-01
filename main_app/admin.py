from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import *

<<<<<<< HEAD
class AbstractUserInline(admin.StackedInline):
    model = AbstractUser
    can_delete = False
    verbose_name_plural = 'AbstractUser'

class UserAdmin(BaseUserAdmin):
    inlines = (AbstractUserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
=======
>>>>>>> 1956836ea3ea19ed48d43eaf9d25d3ef4eb2bc0e

admin.site.register(TestUserProfile)
admin.site.register(TestUser)
admin.site.register(TestProfession)
admin.site.register(TestSkill)
admin.site.register(TestTask)
