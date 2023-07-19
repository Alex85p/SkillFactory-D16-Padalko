from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
        Пользовательская модель пользователя.

        Поля:
            username (CharField): Имя пользователя (логин).
            password (CharField): Хэшированный пароль пользователя.
            email (EmailField): Email пользователя.
            verification_code (IntegerField): Код верификации пользователя. (пользовательская добавка)
    """
    verification_code = models.IntegerField(default=0)
