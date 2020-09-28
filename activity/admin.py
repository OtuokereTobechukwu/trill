from django.contrib import admin
from .models import Post
# Register your models here.

# admin.site.register(Posts)
@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['author', 'slug', 'image', 'created']
    list_filter = ['created']
