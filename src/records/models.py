from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class CallRequest(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')
    phone = PhoneNumberField(verbose_name='телефон')
    created_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
