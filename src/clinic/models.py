from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


def get_license_image_upload_path(instance: 'License', filename: str) -> str:
    return f'license/{instance.name}/image/{filename}'


def get_license_pdf_upload_path(instance: 'License', filename: str) -> str:
    return f'license/{instance.name}/pdf/{filename}'


class License(models.Model):
    name = models.CharField(verbose_name='название лицензии', max_length=255)
    slug = models.SlugField(max_length=255)

    image = models.ImageField(
        verbose_name='фото документа',
        blank=True,
        null=True,
        upload_to=get_license_image_upload_path,
    )
    pdf = models.FileField(
        verbose_name='pdf файл для просмотра документа',
        blank=True,
        null=True,
        upload_to=get_license_pdf_upload_path,
    )

    published = models.BooleanField(
        verbose_name='является ли опубликованным',
        blank=True,
        default=True,
    )

    class Meta:
        verbose_name = 'лицензия'
        verbose_name_plural = 'лицензии'

    def __str__(self):
        return self.name


class About(models.Model):
    about = CKEditor5Field(
        verbose_name='о клинике',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'О клинике'
        verbose_name_plural = 'О клинике'


class Details(models.Model):
    full_name = models.CharField(verbose_name='Полное наименование', max_length=255)
    abbreviated_name = models.CharField(verbose_name='Сокращенное наименование', max_length=255)
    INN_KPP = models.CharField(verbose_name='ИНН/КПП', max_length=255)
    OGRN = models.CharField(verbose_name='ОГРН', max_length=255)
    legal_address = models.CharField(verbose_name='Юридический адрес', max_length=255)
    actual_address = models.CharField(verbose_name='Фактический адрес', max_length=255)
    telephone = models.CharField(verbose_name='Телефон', max_length=255)
    fax = models.CharField(verbose_name='факс', max_length=255)
    email = models.CharField(verbose_name='Электронная почта', max_length=255)
    website = models.CharField(verbose_name='Сайт', max_length=255)
    bank_details = models.CharField(verbose_name='Банковские реквизиты', max_length=255)

    class Meta:
        verbose_name = 'реквизиты'
        verbose_name_plural = 'реквизиты'

    def __str__(self):
        return self.full_name


class Contact(models.Model):
    address = models.CharField(
        verbose_name='адрес',
        max_length=255,
    )
    opening_hours = models.CharField(
        verbose_name='Часы работы',
        max_length=255,
    )
    phone_numbers = models.CharField(verbose_name='Номера телефонов', max_length=255)
    email = models.EmailField(verbose_name='почта', max_length=255)

    def __str__(self):
        return self.address


class Media(models.Model):
    tg = models.URLField(
        verbose_name='телеграм',
        max_length=255,
    )
    whatsapp = models.URLField(
        verbose_name='ватсап',
        max_length=255,
    )
    vk = models.URLField(
        verbose_name='вк',
        max_length=255,
    )
    whatsapp = models.URLField(
        verbose_name='ватсап',
        max_length=255,
    )
