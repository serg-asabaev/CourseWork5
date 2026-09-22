from django.contrib.auth.models import (AbstractUser, PermissionsMixin,
                                        UserManager)
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Введите номер телефона",
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Введите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите свой аватар",
    )

    last_login = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Дата последнего входа',
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    is_staff = models.BooleanField(default=False)

    tg_chat_id = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Телеграм chat-id",
        help_text="Укажите телеграм chat-id"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    objects = UserManager()