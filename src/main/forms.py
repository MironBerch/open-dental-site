from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск')

    class Meta:
        fields = ('query',)
        widgets = {
            'query': forms.TextInput(attrs={'placeholder': ''}),
        }
