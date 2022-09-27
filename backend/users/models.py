from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    """Расширенная модель User."""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    email = models.EmailField(
        db_index=True,
        unique=True,
        max_length=254,
        verbose_name='Email пользователя',
        help_text='Укажите email пользователя'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Пользователь {self.email}'


User = MyUser


class Follow(models.Model):
    """Модель подписок на авторов."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
        related_name='follower',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Подписка',
        related_name='following',
    )

    class Meta:
        verbose_name = 'Подписки'

    def __str__(self):
        return f"{self.user} подписан на {self.following}"
