from .models import DataBase
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class DataBaseForm(ModelForm):
    class Meta:
        model = DataBase
        fields = ['title', 'anons', 'full_test', 'data']

        widgets = {
            "title":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nomlanishi'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons'
            }),
            "full_test": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Maqolalar...'
            }),
            "data": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Maqola sanasi'
            }),
        }