from django_ckeditor_5.fields import CKEditor5Field
from phonenumber_field.modelfields import PhoneNumberField

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


def get_license_image_upload_path(instance: 'License', filename: str) -> str:
    return f'license/{instance.name}/image/{filename}'


def get_license_pdf_upload_path(instance: 'License', filename: str) -> str:
    return f'license/{instance.name}/pdf/{filename}'


def get_staff_image_upload_path(instance: 'Staff', filename: str) -> str:
    return f'staff/{instance.fio}/{filename}'


class PositionChoices(models.TextChoices):
    MANAGER = 'Руководитель', 'Руководитель'
    ADMINISTRATOR = 'Администратор', 'Администратор'
    MEDIC = 'Мед персонал', 'Мед персонал'
    JUNIOR_MEDIC = 'Младщий мед персонал', 'Младщий мед персонал'


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
        blank=True,
    )
    opening_hours = models.CharField(
        verbose_name='Часы работы',
        max_length=255,
        blank=True,
    )
    phone_numbers = models.CharField(
        verbose_name='Номера телефонов',
        max_length=255,
        blank=True,
    )
    email = models.EmailField(
        verbose_name='почта',
        max_length=255,
        blank=True,
    )

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.address


class Media(models.Model):
    tg = models.URLField(
        verbose_name='телеграм',
        max_length=255,
        blank=True,
    )
    whatsapp = models.URLField(
        verbose_name='ватсап',
        max_length=255,
        blank=True,
    )
    vk = models.URLField(
        verbose_name='вк',
        max_length=255,
        blank=True,
    )

    class Meta:
        verbose_name = 'Ссылки на социальные сети и контакты'
        verbose_name_plural = 'Ссылки на социальные сети и контакты'


class Policy(models.Model):
    text = CKEditor5Field(
        verbose_name='текст',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Соглашение на обработку данных'
        verbose_name_plural = 'Соглашения на обработку данных'


def get_review_image_upload_path(instance: 'Review', filename: str) -> str:
    return f'review/{instance.email}/{filename}'


class Review(models.Model):
    name = models.CharField(verbose_name='имя', max_length=255)
    email = models.EmailField(
        verbose_name='почта',
        null=True,
        blank=True,
        max_length=255,
    )
    phone = PhoneNumberField(verbose_name='номер телефона', blank=True, null=True)

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
