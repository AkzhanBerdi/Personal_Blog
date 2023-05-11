from django import forms
from website.models import Comment, Author, Tag


class GenreForm(forms.Form):
    title = forms.CharField(
        max_length=50,
        min_length=3,
        required=True,
        label='Genre name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Input Genre name"
        })
    )
    description = forms.CharField(
        max_length=500,
        min_length=10,
        required=True,
        label='Genre description',
        widget=forms.Textarea(attrs={
            'rows': 4,
            'class': 'form-control'
        })
    )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text','author',)

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Article name')
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=True, label='Author', widget=forms.Select)
    body = forms.CharField(max_length=3500, required=True, widget=forms.Textarea, label='Article text')
    tags = forms.ModelMultipleChoiceField(required=False, label='Tags', queryset=Tag.objects.all())