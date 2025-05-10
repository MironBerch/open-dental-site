from django_ckeditor_5.fields import CKEditor5Field

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from main.fields import WebPImageField


def get_service_image_upload_path(instance: 'Service', filename: str) -> str:
    return f'services/{instance.name}/{filename}'


def get_work_image_upload_path(instance: 'Work', filename: str) -> str:
    return f'work_previews/{instance.name}/{filename}'


def get_photo_image_upload_path(instance: 'Photo', filename: str) -> str:
    return f'works/{instance.work.name}/{filename}'


def get_staff_image_upload_path(instance: 'Staff', filename: str) -> str:
    return f'staff/{instance.fio}/{filename}'


def get_license_image_upload_path(instance: 'License', filename: str) -> str:
    return f'license/{instance.name}/image/{filename}'


def get_license_pdf_upload_path(instance: 'License', filename: str) -> str:
    return f'license/{instance.name}/pdf/{filename}'


class License(models.Model):
    name = models.CharField(verbose_name='название лицензии', max_length=255)
    image = WebPImageField(
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
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.address


class Policy(models.Model):
    text = CKEditor5Field(
        verbose_name='текст',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Соглашение на обработку данных'
        verbose_name_plural = 'Соглашения на обработку данных'


class Review(models.Model):
    name = models.CharField(verbose_name='имя', max_length=255)
    message = models.TextField(verbose_name='сообщение', blank=True, null=True)
    rating = models.PositiveIntegerField(
        verbose_name='оценка',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )
    published = models.BooleanField(
        verbose_name='является ли опубликованным',
        blank=True,
        default=True,
    )
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.name} - {self.rating}'


class Staff(models.Model):
    image = WebPImageField(
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


class PriceGroup(models.Model):
    name = models.CharField(verbose_name='название', unique=True, max_length=255)

    class Meta:
        verbose_name = 'Группа цен'
        verbose_name_plural = 'Группы цен'

    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=255,
        unique=True,
    )
    cost = models.PositiveIntegerField(verbose_name='цена')
    constant = models.BooleanField(default=False, verbose_name='постоянная')
    group = models.ForeignKey(
        PriceGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='группа цен',
    )
    published = models.BooleanField(
        verbose_name='является ли опубликованным',
        blank=True,
        default=True,
    )

    class Meta:
        verbose_name = 'цена'
        verbose_name_plural = 'цены'

    def __str__(self) -> str:
        return f'{self.name} [{self.group.name}] - {self.cost})'


class ServiceGroup(models.Model):
    name = models.CharField(verbose_name='название', unique=True, max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    short_description = models.TextField(
        verbose_name='краткое описание',
        blank=True,
        null=True,
    )
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
    image = WebPImageField(
        verbose_name='фото документа',
        blank=True,
        null=True,
        upload_to=get_service_image_upload_path,
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


class Work(models.Model):
    image = WebPImageField(
        verbose_name='Превью',
        upload_to=get_work_image_upload_path,
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
    image = WebPImageField(upload_to=get_photo_image_upload_path)

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фото'

    def __str__(self) -> str:
        return f'Фото для {self.work.name}'
