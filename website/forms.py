from django import forms
from website.models import Comment, Author, Genre, Article
from django.core.exceptions import ValidationError


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
        fields = ('text','author',)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=200, required=True, label='Article name', validators=(at_least_5, ))
    
    class Meta:
         model = Article
         fields = "__all__"

    def clean_author(self):
        author = self.cleaned_data['author']
        if author.id == 1:
            raise ValidationError(f'Author {author} has an article')
        return author

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('title') == cleaned_data.get('body'):
            raise ValidationError('Article and Text should be different')

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError('Article is too short')
        return title

class SearchFrom(forms.Form):
    serach = forms.CharField(max_length=100, required=False, label='Search')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        firleds = '__all__'