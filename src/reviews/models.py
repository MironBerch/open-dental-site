from phonenumber_field.modelfields import PhoneNumberField

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


def get_review_image_upload_path(instance: 'Review', filename: str) -> str:
    return f'review/{instance.email}/{filename}'


class Review(models.Model):
    name = models.CharField(verbose_name='имя', max_length=255)
    email = models.EmailField(verbose_name='почта', max_length=255)
    phone = PhoneNumberField(verbose_name='номер телефона', blank=True)

    message = models.TextField(verbose_name='сообщение', blank=True, null=True)

    rating = models.PositiveIntegerField(
        verbose_name='оценка',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )

    image = models.ImageField(
        verbose_name='фото',
        blank=True,
        null=True,
        upload_to=get_review_image_upload_path,
    )

    published = models.BooleanField(
        verbose_name='является ли опубликованным',
        blank=True,
        default=True,
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.name} - {self.rating}'
