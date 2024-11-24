from django_ckeditor_5.fields import CKEditor5Field

from django.db import models


def get_staff_image_upload_path(instance: 'Work', filename: str) -> str:
    return f'works/{instance.id}/{filename}'


class Work(models.Model):
    image = models.ImageField(
        verbose_name='Превью',
        upload_to='works/previews/',
        blank=True,
        null=True,
    )
    name = models.CharField(
        verbose_name='название',
        max_length=100,
        unique=True,
    )
    slug = models.SlugField(unique=True, max_length=255)
    information = CKEditor5Field(
        verbose_name='информация',
        blank=True,
        null=True,
    )
    published = models.BooleanField(
        verbose_name='является ли опубликованным',
        blank=True,
        default=True,
    )

    class Meta:
        verbose_name = 'работа'
        verbose_name_plural = 'работы'

    def __str__(self) -> str:
        return self.name


class Photo(models.Model):
    work = models.ForeignKey(Work, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_staff_image_upload_path)

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фото'

    def __str__(self) -> str:
        return f'Фото для {self.work.name}'
