from django import forms
from django.core.exceptions import ValidationError

from .models import Comment, Author, Genre, Article

def at_least_5(string):
    if len(string) < 5:
        raise ValidationError("It's too short")

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=200, required=True, label='Article name', validators=(at_least_5, ))
    
    class Meta:
         model = Article
         fields = ('author', )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('title') == cleaned_data.get('body'):
            raise ValidationError('Article and Text should be different')

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError('Article is too short')
        return title

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Search')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'