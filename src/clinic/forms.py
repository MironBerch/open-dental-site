from django import forms

from clinic.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'message', 'rating', )
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': ''}),
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': ''}),
            'rating': forms.Select(
                choices=[(i, i) for i in range(1, 6)],
                attrs={'class': 'rating-select'},
            ),
        }
        labels = {
            'name': 'Ваше имя*',
            'message': 'Сообщение*',
            'rating': 'Оценка*',
        }
