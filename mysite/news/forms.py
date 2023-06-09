from .models import Articles
from django.forms import ModelForm, TextInput,  Textarea, DateTimeInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'content', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            })
        }