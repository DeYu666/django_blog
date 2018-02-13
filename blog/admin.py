from django.contrib import admin

# Register your models here.
from .models import Post, Category, TopCate


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'category', 'author', 'comments_num', 'like_num']


class CateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'topcate', 'cover_image']


class TopCateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CateAdmin)
admin.site.register(TopCate, TopCateAdmin)