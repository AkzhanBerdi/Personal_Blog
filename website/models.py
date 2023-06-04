from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Author's first name")
    last_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Author's last name")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='title')
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.SET_DEFAULT,
        default = 1,
        related_name = 'article',
        verbose_name = 'Author'
    )
    body = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Text')
    is_deleted = models.BooleanField(default=False, verbose_name='Deleted')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date and Time created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date and Time updated')
    tags = models.ManyToManyField(
        'website.Tag', 
        related_name='articles',
        blank=True
    )
    
    def __str__(self):
        return f"{self.pk}.{self.title}"

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        permissions = [
            ('can_read_article', '有权限读文章')
        ]

class Genre(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=1000, null=False, blank=False, default='default description', verbose_name='Description')

    def __str__(self):
        return f'{self.pk}. {self.title}'

class Comment(models.Model):
    article = models.ForeignKey('website.Article', on_delete=models.CASCADE, related_name ='comments', verbose_name= 'Article')
    text = models.TextField(max_length=500, verbose_name='Comments')
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.SET_DEFAULT,
        default = 1,
        related_name = 'comment',
        verbose_name='Author'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'created date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'updated date')

    def __str__(self):
        return self.text[:20]

class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Tag')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date and Time')

    def __str__(self):
        return self.name