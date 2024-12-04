from phonenumber_field.modelfields import PhoneNumberField

from django.db import models


class CallRequest(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')
    phone = PhoneNumberField(verbose_name='телефон')
    created_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Вызов звонка'
        verbose_name_plural = 'Вызовы звонков'

    def __str__(self):
        return f'{self.name} - {self.phone} - {self.processed}'
