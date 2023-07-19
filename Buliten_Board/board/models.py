from django.db import models
from django.urls import reverse

from accounts.models import CustomUser as User


class Listing(models.Model):
    """
    Модель объявления.

    Атрибуты:
        author (ForeignKey): Внешний ключ, связывающий объявление с пользователем-автором. При удалении
                             пользователя, связанные с ним объявления также будут удалены.
        dateCreation (DateTimeField): Поле, хранящее дату и время создания объявления. Автоматически
                                     заполняется текущей датой и временем при создании записи.
        category (CharField): Поле с выбором категории объявления из предопределенных вариантов.
        title (CharField): Поле для заголовка объявления (максимальная длина 100 символов).
        text (TextField): Поле для текстового описания объявления.
        image1 (ImageField): Поле для загрузки изображения 1, связанного с объявлением (необязательное поле).
        image2 (ImageField): Поле для загрузки изображения 2, связанного с объявлением (необязательное поле).

    Примечание:
        - Категории объявлений заданы в виде кортежа `CATEGORY_CHOICES`, где первый элемент каждой пары -
          значение для хранения в базе данных, а второй элемент - отображаемое имя категории для пользователей.
        - Для обработки изображений модель использует поля `ImageField` для загрузки и хранения изображений.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCreation = dateCreation = models.DateTimeField(auto_now_add=True)
    CATEGORY_CHOICES = (
        ('tank', 'Танки'),
        ('healer', 'Хилы'),
        ('dd', 'ДД'),
        ('trader', 'Торговцы'),
        ('guild_master', 'Гилдмастеры'),
        ('quest_giver', 'Квестгиверы'),
        ('blacksmith', 'Кузнецы'),
        ('leatherworker', 'Кожевники'),
        ('alchemist', 'Зельевары'),
        ('spellcaster', 'Мастера заклинаний'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=100)
    text = models.TextField()
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)

    def get_category_display_ru(self):
        category_choices = dict(self.CATEGORY_CHOICES)
        return category_choices.get(self.category, '')

    def get_absolute_url(self):
        return reverse('listing_detail', args=[str(self.id)])


class Reply(models.Model):
    """
    Модель отклика на объявление.

    Атрибуты:
        listing (ForeignKey): Внешний ключ, связывающий отклик с объявлением. При удалении объявления,
                              связанные с ним отклики также будут удалены.
        author (ForeignKey): Внешний ключ, связывающий отклик с пользователем-автором. При удалении
                             пользователя, связанные с ним отклики также будут удалены.
        text (TextField): Поле для текстового содержания отклика.
        status (BooleanField): Поле, определяющее статус отклика (True - принят, False - не принят).
                              По умолчанию устанавливается в значение False.

    Примечание:
        - Статус отклика определяет, был ли он принят автором объявления или нет.
        - Поля `listing` и `author` связаны с моделями `Listing` и `User` соответственно с помощью
          внешних ключей `ForeignKey`.
    """
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.BooleanField(default=False)
