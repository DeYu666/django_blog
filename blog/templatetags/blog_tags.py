from ..models import Post, Category
from django import template

register = template.Library()


@register.simple_tag
def get_recent_posts(num=6):  # 最新博客标签（内容5条）
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_hots_posts(num=15):   # 热门点击标签（内容15条）
    return Post.objects.all().order_by('-like_num')[:num]


@register.simple_tag
def get_next_posts(num=0):  # 接下来的内容的标签（内容10条）
    return Post.objects.all().order_by('-id')[num:(num + 10)]


@register.simple_tag
def get_categories():  # 分类模板标签
    return Category.objects.all()


@register.simple_tag
def archives():   # 归档标签
    return Post.objects.dates('created_time', 'month', order='DESC')



"""
    首页
        最新博客标签（内容5条）
        热门点击标签（内容15条）
    分类
        分类标签
        下一页标签
    内容
        接下来的内容的标签（内容10条）
"""