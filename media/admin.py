from django.contrib import admin
from .models import Book, Video
# Register your models here.

class BookInline(admin.TabularInline):
    model = Book

class SkillAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]
    fields = ('name', 'title')
admin.site.register(Book)
admin.site.register(Video)

