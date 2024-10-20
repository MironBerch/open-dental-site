from django.db import models


def get_staff_image_upload_path(instance: 'Staff', filename: str) -> str:
    return f'upload/{instance.fio}/{filename}'


class PositionChoices(models.TextChoices):
    MANAGER = 'Руководитель', 'Руководитель'
    ADMINISTRATOR = 'Администратор', 'Администратор'
    MEDIC = 'Мед персонал', 'Мед персонал'
    JUNIOR_MEDIC = 'Младщий мед персонал', 'Младщий мед персонал'


class Role(models.Model):
    name = models.CharField(verbose_name='название', max_length=50)

    class Meta:
        verbose_name = 'роль или специализация'
        verbose_name_plural = 'роли или специализации'

    def __str__(self):
        return self.name


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
    information = models.TextField(
        verbose_name='информация',
        blank=True,
        null=True,
    )

    roles = models.ManyToManyField(
        Role,
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
