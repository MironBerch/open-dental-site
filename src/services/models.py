from django.db import models


class Tag(models.Model):
    name = models.CharField(verbose_name='название', max_length=50)

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
    information = models.TextField(
        verbose_name='информация',
        blank=True,
        null=True,
    )

    tag = models.ForeignKey(
        Tag,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='тэг',
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
