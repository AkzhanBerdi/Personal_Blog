from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), 
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    birthdate = models.DateField(null=True, blank=True, verbose_name='birthday date')
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='user_pics',
        verbose_name='Avatar'
    )

    def __str__(self):
        return self.user.get_full_name()


    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'