from django_ckeditor_5.fields import CKEditor5Field

from django.db import models

from clinic.models import Price


def get_license_image_upload_path(instance: 'Service', filename: str) -> str:
    return f'services/{instance.name}/{filename}'


class ServiceGroup(models.Model):
    name = models.CharField(verbose_name='название', unique=True, max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
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
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(unique=True, max_length=255)
    short_information = models.TextField(
        verbose_name='краткая информация',
        blank=True,
        null=True,
    )
    information = CKEditor5Field(
        verbose_name='информация',
        blank=True,
        null=True,
    )

    image = models.ImageField(
        verbose_name='фото документа',
        blank=True,
        null=True,
        upload_to=get_license_image_upload_path,
    )

    prices = models.ManyToManyField(
        Price,
        verbose_name='цены',
        blank=True,
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

    def get_min_price(self):
        """Возвращает минимальную цену услуги."""
        return self.prices.aggregate(models.Min('cost'))['cost__min']
