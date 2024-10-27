from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class ServiceGroup(models.Model):
    name = models.CharField(verbose_name='название', max_length=50)
    description = models.TextField(
        verbose_name='описание',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=100,
        unique=True,
    )
    information = CKEditor5Field(
        verbose_name='информация',
        blank=True,
        null=True,
    )

    group = models.ForeignKey(
        ServiceGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='группа',
    )

    published = models.BooleanField(
        verbose_name='является ли опубликованным',
        blank=True,
        default=True,
    )

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

    def __str__(self) -> str:
        return self.name
