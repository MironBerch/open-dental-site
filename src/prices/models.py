from django.db import models


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
