from .models import reviews
from django.forms import ModelForm, TextInput, Textarea, IntegerField, NumberInput


class reviewsForm(ModelForm):
    class Meta:
        model = reviews
        fields = ['title', 'reviews_text', 'username', 'score']
        widgets = {
            "title": TextInput(attrs={'class': "form-control",
                                      'placeholder': 'Заголовок'}),
            'reviews_text': Textarea(attrs={'class': "form-control",
                                            'placeholder': 'Текст отзыва'}),
            'username': TextInput(attrs={'class': "form-control",
                                         'placeholder': 'Введите имя пользователя'}),
            'score': NumberInput(attrs={'class': 'form-control',
                                        'placeholder': 'Введите оценку'})
        }
