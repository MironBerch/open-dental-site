from phonenumber_field.formfields import PhoneNumberField

from django import forms
from django.core.validators import RegexValidator

from records.models import CallRequest


class CallRequestForm(forms.ModelForm):
    name = forms.CharField(label='Ваше имя*')
    phone = PhoneNumberField(
        label='Телефон*',
        validators=[
            RegexValidator(
                regex=r'^\+?[0-9]{7,15}$',
                message='Номер телефона необходимо ввести в формате: +XXXXXXXXXXXXX.',
            ),
        ],
    )

    class Meta:
        model = CallRequest
        fields = ('name', 'phone')

    def __init__(self, *args, **kwargs):
        super(CallRequestForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = ''
        self.fields['phone'].widget.attrs['placeholder'] = ''
