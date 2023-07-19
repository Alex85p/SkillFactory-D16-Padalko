from django import forms
from django.core.exceptions import ValidationError

from .models import Listing, Reply


class ListingForm(forms.ModelForm):
    """
        Форма для создания и редактирования объявлений.

        Поля:
            category (ChoiceField): Выбор категории объявления.
            title (CharField): Заголовок объявления.
            text (CharField): Текст объявления.
            image1 (ImageField): Первое изображение объявления (необязательно).
            image2 (ImageField): Второе изображение объявления (необязательно).
    """
    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)

    class Meta:
        model = Listing
        fields = ['category', 'title', 'text', 'image1', 'image2']
        labels = {
            'category': 'Категория',
            'title': 'Заголовок',
            'text': 'Текст объявления',
            'image1': 'Изображение1',
            'image2': 'Изображение2',
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if title == text:
            raise ValidationError(
                "Название объявления не должно быть идентично ее содержанию."
            )

        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0].islower():
            raise ValidationError(
                "Название объявления должно начинаться с заглавной буквы"
            )
        return title


class ReplyForm(forms.ModelForm):
    """
        Форма для создания отклика на объявление.

        Поля:
            text (CharField): Текст отклика.
    """
    class Meta:
        model = Reply
        fields = ['text']
        labels = {
            'text': 'Текст отклика',
        }
