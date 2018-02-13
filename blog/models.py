from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class TopCate(models.Model):
    name = models.CharField(max_length=100, default='学无止境')

    def __str__(self):
        return self.name


class Category(models.Model):
    """
     Django 内置的全部类型可查看文档：
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
    name = models.CharField(max_length=100)
    cover_image = models.FileField(upload_to="cover_image/%Y/%m/%d/", blank=True)
    topcate = models.ForeignKey(TopCate, default='0')

    def __str__(self):
        return self.name

    def get_posts_url(self):
        return reverse('blog:cate_list', kwargs={'pk': self.pk})
        pass


class Post(models.Model):
    """
     文章id  	标题  	发表时间 	作者 	正文
	 封面图片  摘要 	分类  	评论数  	喜欢数
    """
    title = models.CharField(max_length=70)
    created_time = models.DateField()
    author = models.ForeignKey(User)
    body = models.TextField()
    cover_image = models.FileField(upload_to="cover_image_son/%Y/%m/%d/", blank=True)
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    comments_num = models.IntegerField(blank=True)
    like_num = models.IntegerField(blank=True)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
