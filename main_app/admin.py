from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(TestUserProfile)
admin.site.register(TestUser)
admin.site.register(TestProfession)
admin.site.register(TestSkill)
admin.site.register(TestTask)
