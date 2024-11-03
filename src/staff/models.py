from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


def get_staff_image_upload_path(instance: 'Staff', filename: str) -> str:
    return f'staff/{instance.fio}/{filename}'


class PositionChoices(models.TextChoices):
    MANAGER = 'Руководитель', 'Руководитель'
    ADMINISTRATOR = 'Администратор', 'Администратор'
    MEDIC = 'Мед персонал', 'Мед персонал'
    JUNIOR_MEDIC = 'Младщий мед персонал', 'Младщий мед персонал'


class Staff(models.Model):
    image = models.ImageField(
        verbose_name='фото работника',
        blank=True,
        null=True,
        upload_to=get_staff_image_upload_path,
    )
    fio = models.CharField(
        verbose_name='ФИО',
        max_length=100,
        unique=True,
    )
    slug = models.SlugField(unique=True, max_length=255)
    information = CKEditor5Field(
        verbose_name='информация',
        blank=True,
        null=True,
    )

    roles = models.CharField(
        max_length=255,
        verbose_name='роли или специализации',
        blank=True,
    )

    stage = models.CharField(
        verbose_name='позиция',
        blank=True,
        max_length=50,
        choices=PositionChoices.choices,
    )

    published = models.BooleanField(
        verbose_name='является ли опубликованным',
        blank=True,
        default=True,
    )

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'

    def __str__(self) -> str:
        return self.fio
