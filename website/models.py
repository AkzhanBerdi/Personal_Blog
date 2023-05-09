from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False, verbose_name="Author's first name")
    last_name = models.CharField(max_length=50, null=False, verbose_name="Author's last name")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='title')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='author')
    body = models.TextField(max_length=3000, null=False, blank=False, verbose_name='text')
    is_deleted = models.BooleanField(default=False, verbose_name='Deleted')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date and Time created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date and Time updated')

    def __str__(self):
        return f"{self.pk}.{self.title}"

class Genre(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Description')


    def __str__(self):
        return f'{self.pk}. {self.title}'

class Comment(models.Model):
    article = models.ForeignKey('website.Article', on_delete=models.CASCADE, related_name ='comments')
    text = models.TextField(max_length=500)
    author = models.CharField(max_length=40, null=True, blank=True, default ='user_007')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'created date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'updated date')

    def __str__(self):
        return self.text[:20]
