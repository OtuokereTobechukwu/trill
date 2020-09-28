from django.contrib import admin
from .models import Posts
# Register your models here.

admin.site.register(Posts)
# class PostsAdmin(admin.ModelAdmin):
#     list_display = ['user', 'slug', 'image', 'created']
#     list_filter = ['created']
