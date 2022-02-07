from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    CHOICES = (
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator'),
        (USER, 'user'),)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    confirmation_code = models.CharField(
        blank=True,
        editable=False,
        null=True,
        max_length=36,
        verbose_name='Код доступа'
    )
    role = models.CharField(max_length=20,
                            choices=CHOICES,
                            default='user',
                            verbose_name='Уровень доступа'
                            )

    bio = models.TextField(blank=True)

    class Meta:
        ordering = ['-username']
        verbose_name = 'user'
        verbose_name_plural = 'users'

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_staff

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR
